from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, database, models


router = APIRouter(
    prefix="/coche",
    tags=['Coche']
)
get_db=database.get_db


@router.get('', response_model=List[schemas.Coche])
def all(db: Session = Depends(database.get_db)):
    coches = db.query(models.Coche).all()
    return coches
    
@router.get('/modelos/{marca_id}', response_model=List[schemas.Modelo])
def allmodelo(marca_id:int, db: Session = Depends(database.get_db)):
    modelos = db.query(models.Modelo).filter(models.Modelo.coche_id == marca_id).all()
    return modelos

@router.post('', response_model=schemas.Coche)
def create(request: schemas.CocheCreate, db: Session=Depends(get_db)):
    new_coche = models.Coche(marca=request.marca)
    db.add(new_coche)
    db.commit()
    db.refresh(new_coche)
    return new_coche

@router.post('/modelo', response_model=schemas.Modelo)
def postmodelo(request: schemas.modeloCreate, db: Session=Depends(get_db)):
    new_modelo = models.Modelo(modelo=request.modelo, coche_id=request.coche_id)
    db.add(new_modelo)
    db.commit()
    db.refresh(new_modelo)
    return new_modelo