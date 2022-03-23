from msilib import schema
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, database, models

router = APIRouter(
    prefix="/empleados",
    tags=['Empleados']
)
get_db=database.get_db

@router.post('', response_model=schemas.Empleado)
def create(request: schemas.EmpleadoCreate, db: Session=Depends(get_db)):
    new_empleado = models.Empleado(name=request.name,
                                    lestname=request.lestname,
                                    telefono=request.telefono,
                                    cedula=request.cedula,
                                    direccion=request.direccion,
                                    codigo_postal=request.codigo_postal)
    db.add(new_empleado)
    db.commit()
    db.refresh(new_empleado)
    return new_empleado

@router.get('', response_model=List[schemas.Empleado])
def get_all(db: Session=Depends(get_db)):
    empleado = db.query(models.Empleado).all()
    return empleado

@router.get('/{id}', response_model=List[schemas.Empleado])
def show(id:int, db: Session = Depends(get_db)):
    empleado = db.query(models.Empleado).filter(models.Empleado.id == id).all()
    
    return empleado