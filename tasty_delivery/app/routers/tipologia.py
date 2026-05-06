from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db
from crud.tipologia import get_tipologie
from crud.ristorante import get_ristorante_per_tipologia
from schemas.tipologia import Tipologia
from schemas.ristorante import Ristorante

router = APIRouter(prefix="/tipologie", tags=['tipologie'])

@router.get("/", response_model=List[Tipologia])
def get_lista_tipologie(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_tipologie(skip, limit, db)

@router.get("/{tipologia_id}/ristoranti", response_model=List[Ristorante])
def get_lista_ristoranti_per_tipologia(tipologia_id: int, db: Session = Depends(get_db)):
    return get_ristorante_per_tipologia(db, tipologia_id)