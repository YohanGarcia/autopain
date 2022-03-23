from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from starlette.responses import Response

from .. import schemas, database, models


router = APIRouter(tags=['Desabolladora'])

get_db=database.get_db

@router.get('/desabolladora/{servicio_id2}', response_model=List[schemas.Desabolladura])
def all_vehiculo(servicio_id2:int, db: Session = Depends(get_db)):
    desabollador = db.query(models.Desabolladura).filter(models.Desabolladura.servicio_id == servicio_id2).all()
    suma = 0
    for i in desabollador:
        suma += i.precio
    print(f"precio total {suma}") 
    return desabollador

@router.post('/desabolladora', response_model=schemas.Desabolladura)
def create(request: schemas.DesabolladutaCreate, db: Session=Depends(get_db)):
    new_servicio = models.Desabolladura(piesa=request.piesa,
                                        precio=request.precio,
                                        servicio_id=request.servicio_id)
    db.add(new_servicio)
    db.commit()
    db.refresh(new_servicio)
    return new_servicio