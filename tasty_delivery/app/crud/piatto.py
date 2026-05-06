from sqlalchemy.orm import Session
from models.piatto import Piatto
from schemas.piatto import PiattoCreate
from crud.ristorante import get_ristorante

def get_menu_ristorante(db: Session, ristorante_id: int):
    ristorante = get_ristorante(db, ristorante_id)
    return ristorante.piatto

def crea_piatto(db: Session, piatto: PiattoCreate):
    get_ristorante(db, piatto.ristorante_id) # verifica esistenza
    nuovo_piatto = Piatto(**piatto.model_dump())
    db.add(nuovo_piatto)
    db.commit()
    db.refresh(nuovo_piatto)
    return nuovo_piatto