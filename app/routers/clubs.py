from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import percent_rank
from app import models, schemas, utils
from app.database import get_db

router = APIRouter(
    tags = ['Clubs'],
    prefix="/clubs"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ClubsOut)
def create_clubs(gps: schemas.ClubsOut, db: Session = Depends(get_db)):
    #hash the Password
    new_club = models.Gps(**gps.dict())
    db.add(new_club)
    db.commit()
    db.refresh(new_club)
    return new_club