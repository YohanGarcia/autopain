from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from starlette.responses import Response

from .. import schemas, database, models
#from ..repostory import blog

router = APIRouter(
    prefix="/clientes",
    tags=['Cliente']
)
get_db=database.get_db

@router.get('', response_model=List[schemas.Cliente])
async def all(db: Session = Depends(get_db)):
    clientes = db.query(models.Cliente).all()

    return clientes

@router.post('', response_model=schemas.Cliente)
def create(request: schemas.ClienteCreate, db: Session=Depends(get_db)):
    new_cliente = models.Cliente(name=request.name, 
                                lestname=request.lestname, 
                                telefono=request.telefono,
                                cedula=request.cedula)
    db.add(new_cliente)
    db.commit()
    db.refresh(new_cliente)
    return new_cliente

@router.delete('/{id}')
async def destroy(id:int, db: Session=Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == id)

    cliente.delete(synchronize_session=False)
    db.commit()
    return ' Cliente eliminado'

@router.put('/{id}')
def update_blog(id, request: schemas.Cliente, db: Session=Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == id)

    if not cliente.first():

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    cliente.update(request.__dict__, synchronize_session=False)
    db.commit()

    return 'update'


@router.get('/{id}', response_model=List[schemas.Cliente])
async def show(id:int, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == id).all()
    
    return cliente
