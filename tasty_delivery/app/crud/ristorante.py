from sqlalchemy.orm import Session
from models.ristorante import Ristorante
from schemas.ristorante import RistoranteCreate
from crud.tipologia import get_tipologia


# ------------------------------   GET   -----------------------------
# Restituisce tutti i ristoranti
def get_ristoranti(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Ristorante).offset(skip).limit(limit).all()

# Restituisce un ristorante tramite id
def get_ristorante(db: Session, ristorante_id: int):
    ristorante = db.query(Ristorante).filter(Ristorante.ristorante_id == ristorante_id).first()
    if not ristorante:
        return None
    return ristorante

# Restituisce ristoranti tramite id della tipologia
def get_ristorante_per_tipologia(db: Session, tipologia_id: int):
    tipologia = get_tipologia(db, tipologia_id)
    return tipologia.ristorante