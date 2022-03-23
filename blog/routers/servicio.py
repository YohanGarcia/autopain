from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from starlette.responses import Response

from .. import schemas, database, models


router = APIRouter(tags=['Servicios'])

get_db=database.get_db

@router.get('/servicios', response_model=List[schemas.Servicio])
def all_vehiculo(db: Session = Depends(get_db)):
    servicio = db.query(models.Servicio).all()
    return servicio

@router.get('/servicio/{id}', response_model=List[schemas.Servicio])
async def show(id:int, db: Session = Depends(get_db)):
    servicio = db.query(models.Servicio).filter(models.Servicio.vehiculo_id == id).all()
    return servicio

@router.post('/servicios', response_model=schemas.Servicio)
def create(request: schemas.ServiciosCreate, db: Session=Depends(get_db)):
    new_servicio = models.Servicio(typo=request.typo, vehiculo_id=request.vehiculo_id)
    db.add(new_servicio)
    db.commit()
    db.refresh(new_servicio)
    return new_servicio