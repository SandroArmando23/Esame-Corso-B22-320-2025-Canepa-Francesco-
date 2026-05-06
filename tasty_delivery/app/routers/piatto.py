from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.piatto import Piatto, PiattoCreate
from dependencies import get_db
from crud.piatto import crea_piatto


router = APIRouter(prefix="/piatti", tags=['piatti'])

@router.post("/", response_model=Piatto, status_code=201)
def crea_nuovo_piatto(piatto: PiattoCreate, db: Session = Depends(get_db)):
    return crea_piatto(db, piatto)