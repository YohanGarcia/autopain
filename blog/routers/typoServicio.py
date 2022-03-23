from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas, database, models
#from ..repostory import blog

router = APIRouter(
    prefix="/typo",
    tags=['Typo']
)
get_db=database.get_db

@router.get('', response_model=List[schemas.Typo])
async def all(db: Session = Depends(get_db)):
    typo = db.query(models.Typo).all()
    return typo


@router.post('', response_model=schemas.Typo)
def create(request: schemas.TypoCreate, db: Session=Depends(get_db)):
    new_typo = models.Typo(name=request.name)
    db.add(new_typo)
    db.commit()
    db.refresh(new_typo)
    return new_typo
