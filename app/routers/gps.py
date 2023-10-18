from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import percent_rank
from app import models, schemas, utils
from app.database import get_db

router = APIRouter(
    tags = ['Gps'],
    prefix="/gps"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.GpsOut)
def create_gps(gps: schemas.GpsCreate, db: Session = Depends(get_db)):
    #hash the Password
    new_gps = models.Gps(**gps.dict())
    db.add(new_gps)
    db.commit()
    db.refresh(new_gps)
    return new_gps

@router.get('/{id}', status_code=status.HTTP_201_CREATED, response_model=schemas.GpsOut)
def get_gps(id: int, db: Session = Depends(get_db) ):
    gps = db.query(models.Gps).filter( models.Gps.gps_id == str(id) ).first()
    if gps == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Gps: {id} was not found.")
    return gps