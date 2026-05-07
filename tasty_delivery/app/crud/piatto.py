from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.piatto import Piatto
from schemas.piatto import PiattoCreate
from crud.ristorante import get_ristorante

def get_menu_ristorante(db: Session, ristorante_id: int):
    ristorante = get_ristorante(db, ristorante_id)
    if not ristorante:
        raise HTTPException(status_code=404, detail="Ristorante non trovato")
    return ristorante.piatto

def crea_piatto(db: Session, piatto: PiattoCreate):
    ristorante = get_ristorante(db, piatto.ristorante_id)
    if not ristorante:
        raise HTTPException(status_code=404, detail="Ristorante non trovato")
    nuovo_piatto = Piatto(**piatto.model_dump())
    db.add(nuovo_piatto)
    db.commit()
    db.refresh(nuovo_piatto)
    return nuovo_piatto