from hashlib import new
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, database, models

router = APIRouter(
    prefix="/asignacion",
    tags=['Asignacion']
)
get_db=database.get_db

@router.get('', response_model=List[schemas.Asignacion])
def get_all(db: Session = Depends(get_db)):
    asignacion = db.query(models.Asignacion).all()
    return asignacion


@router.post('', response_model=schemas.Asignacion)
def create(request: schemas.AsignacionCreate, db: Session=Depends(get_db)):

    new_asignacion = models.Asignacion(tipo_trabjo=request.tipo_trabjo,
                                        precio_trabajo=request.precio_trabajo,
                                        empleados_id=request.empleados_id,
                                        desabolladura_id=request.desabolladura_id,
                                        vehiculo_id=request.vehiculo_id)
    db.add(new_asignacion)
    db.commit()
    db.refresh(new_asignacion)
    return new_asignacion

@router.get('/{vehiculo_id}', response_model=List[schemas.Asignacion])
def get_all(vehiculo_id:int, db: Session = Depends(get_db)):
    asignacion = db.query(models.Asignacion).filter(models.Asignacion.vehiculo_id == vehiculo_id).all()
    for i in asignacion:
        print(i.empleados.name)
    return asignacion




@router.delete('/{id}')
async def destroy(id:int, db: Session=Depends(get_db)):
    cliente = db.query(models.Asignacion).filter(models.Asignacion.id == id)

    cliente.delete(synchronize_session=False)
    db.commit()
    return ' Cliente eliminado'