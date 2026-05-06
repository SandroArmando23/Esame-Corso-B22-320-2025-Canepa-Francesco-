from sqlalchemy.orm import Session
from models.tipologia import Tipologia

# ------------------------------   GET   -----------------------------
# Restituisce tutte le tipologie
def get_tipologie(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tipologia).offset(skip).limit(limit).all()

# Restituisce una tipologia tramite id
def get_tipologia(db: Session, tipologia_id: int):
    tipologia = db.query(Tipologia).filter(Tipologia.tipologia_id == tipologia_id).first()
    if not tipologia:
        return None
    return tipologia


