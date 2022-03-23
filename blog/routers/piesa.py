from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, database, models
#from ..repostory import blog

router = APIRouter(
    prefix="/piesa",
    tags=['Piesa']
)
get_db=database.get_db

@router.get('', response_model=List[schemas.Piesa])
async def all(db: Session = Depends(get_db)):
    clientes = db.query(models.Piesa).all()
    return clientes

@router.get('/preciopiesa/{piesa_id}', response_model=List[schemas.Preciopiesa])
def allpreciopies(piesa_id:int, db: Session = Depends(database.get_db)):
    precio = db.query(models.Preciopiesa).filter(models.Preciopiesa.piesa_id == piesa_id).all()
    return precio

@router.post('', response_model=schemas.Piesa)
def create(request: schemas.PiesaCreate, db: Session=Depends(get_db)):
    new_piesa = models.Piesa(piesa=request.piesa)
    db.add(new_piesa)
    db.commit()
    db.refresh(new_piesa)
    return new_piesa

@router.post('/preciopiesa', response_model=schemas.Preciopiesa)
def postpreciopiesa(request: schemas.PreciopiesCreate, db: Session=Depends(get_db)):
    new_precio = models.Preciopiesa(precio=request.precio, piesa_id=request.piesa_id)
    db.add(new_precio)
    db.commit()
    db.refresh(new_precio)
    return new_precio