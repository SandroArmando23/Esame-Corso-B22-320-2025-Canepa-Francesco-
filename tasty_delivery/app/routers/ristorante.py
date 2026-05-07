from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db
from schemas.ristorante import Ristorante
from crud.ristorante import get_ristoranti
from schemas.piatto import Piatto
from crud.piatto import get_menu_ristorante



router = APIRouter(prefix="/ristoranti", tags=['ristoranti'])

@router.get("/", response_model=List[Ristorante])
def lista_ristoranti(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lista = get_ristoranti(db, skip, limit)
    return lista


@router.get("/{ristorante_id}/menu", response_model=List[Piatto])
def menu_ristorante(ristorante_id: int, db: Session = Depends(get_db)):
    menu = get_menu_ristorante(db, ristorante_id)
    if not menu:
        raise HTTPException(status_code=404, detail=f"Menu del ristorante {ristorante_id} non trovato")
    return menu