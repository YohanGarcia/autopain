from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from starlette.responses import Response

from .. import schemas, database, models


router = APIRouter(tags=['Vehiculos'])


get_db=database.get_db

@router.get('/vehiculos', response_model=List[schemas.Vehiculo])
def all_vehiculo(db: Session = Depends(database.get_db)):
    vehiculos = db.query(models.Vehiculo).all()
    return vehiculos


@router.get('/vehiculo/{id}', response_model=List[schemas.Vehiculo])
async def show(id:int, db: Session = Depends(get_db)):
    vehiculo = db.query(models.Vehiculo).filter(models.Vehiculo.cliente_id == id).all()
    
    return vehiculo

@router.post('/vehiculo/{id}/{cliente}', response_model=schemas.Vehiculo)
def create(id:int, request: schemas.VehiculoCreate, db: Session=Depends(get_db)):
    new_vehiculo = models.Vehiculo(modelo=request.modelo, 
                                    marca=request.marca, 
                                    color=request.color, 
                                    placa=request.placa, 
                                    age=request.age, 
                                    cliente_id=id)
    db.add(new_vehiculo)
    db.commit()
    db.refresh(new_vehiculo)
    return new_vehiculo