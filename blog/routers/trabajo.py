from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, database, models

router = APIRouter(
    prefix="/trabajos",
    tags=['Trabajos']
)
get_db=database.get_db

@router.get('', response_model=List[schemas.Trabajo])
def get_all(db: Session=Depends(get_db)):
    trabajo = db.query(models.Trabajo).all()
    return trabajo

@router.get('/preciotrabajo/{trabajo_id}', response_model=List[schemas.PrecioTrabajo])
def allpreciopies(trabajo_id:int, db: Session = Depends(database.get_db)):
    precio = db.query(models.Preciotrabajo).filter(models.Preciotrabajo.trabajo_id == trabajo_id).all()
    return precio

@router.post('', response_model=schemas.Trabajo)
def create(request: schemas.TrabajoCreate, db: Session=Depends(get_db)):
    new_trabajo = models.Trabajo(trabajo_tipo=request.trabajo_tipo)
    db.add(new_trabajo)
    db.commit()
    db.refresh(new_trabajo)
    return new_trabajo

@router.post('/preciotrabajos', response_model=schemas.PrecioTrabajo)
def preciotrabajos(request: schemas.PreciosTrabajoCreate, db: Session=Depends(get_db)):
    new_precio = models.Preciotrabajo(precio=request.precio, trabajo_id=request.trabajo_id)
    db.add(new_precio)
    db.commit()
    db.refresh(new_precio)
    return new_precio