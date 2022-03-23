from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, database, models
#from ..repostory import blog

router = APIRouter(
    prefix="/materiales",
    tags=['Material']
)
get_db=database.get_db


@router.get('', response_model=List[schemas.Material])
def get_piesa(db: Session=Depends(get_db)):
    piesas = db.query(models.Material).all()
    return piesas

@router.post('', response_model=schemas.Material)
def create_material(request: schemas.MaterialCreate, db: Session=Depends(get_db)):
    print(request.name)
    new_material = models.Material(name=request.name)
    db.add(new_material)
    db.commit()
    db.refresh(new_material)
    return new_material

@router.post('/numero', response_model=schemas.Materialnumero)
def create_material_numero(request: schemas.MaterialnumeroCreate, db: Session=Depends(get_db)):
    new_material_numero = models.Materialnumero(numero=request.numero, precio=request.precio, matrales_id=request.matrales_id)
    db.add(new_material_numero)
    db.commit()
    db.refresh(new_material_numero)
    return new_material_numero

