from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db
from schemas.ordine import OrdineCreate, Ordine
from crud.ordine import crea_ordine, get_ordini

router = APIRouter(prefix="/ordini", tags=['ordini'])

@router.post("/", response_model=Ordine, status_code=201)
def crea_nuovo_ordine(ordine: OrdineCreate, db: Session = Depends(get_db)):
    return crea_ordine(db, ordine)

@router.get("/", response_model=List[Ordine])
def get_lista_ordini(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_ordini(skip, limit, db)