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
def create_clubs(clubs: schemas.ClubsCreate, db: Session = Depends(get_db)):
    new_club = models.Clubs(**clubs.dict())
    db.add(new_club)
    db.commit()
    db.refresh(new_club)
    return new_club

@router.get('/{id}', status_code=status.HTTP_201_CREATED, response_model=schemas.ClubsOut)
def get_user(id: int, db: Session = Depends(get_db) ):
    club = db.query(models.Clubs).filter( models.Clubs.club_id == str(id) ).first()
    if club == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Club: {id} was not found.")
    return club