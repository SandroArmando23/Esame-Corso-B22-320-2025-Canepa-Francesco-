from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.ordine import Ordine
from models.dettaglio_ordine import DettaglioOrdine
from models.cliente import Cliente
from models.piatto import Piatto
from schemas.ordine import OrdineCreate
from crud.ristorante import get_ristorante

def get_ordini(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Ordine).offset(skip).limit(limit).all()

def crea_ordine(db: Session, ordine: OrdineCreate):
    # Verifica cliente
    cliente = db.query(Cliente).filter(Cliente.id == ordine.cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente non trovato")
    
    # Verifica ristorante
    get_ristorante(db, ordine.ristorante_id)
    
    # Crea testata ordine
    nuovo_ordine = Ordine(
    cliente_id=ordine.cliente_id,
    ristorante_id=ordine.ristorante_id,
    stato="In preparazione"
    )
    db.add(nuovo_ordine)
    db.flush()
    
    # Inserisce i dettagli (bonus)
    for dettaglio in ordine.dettagli:
        if dettaglio.quantita <= 0:
            raise HTTPException(status_code=400, detail="La quantità deve essere maggiore di 0")
    piatto = db.query(Piatto).filter(Piatto.id == dettaglio.piatto_id).first()
    if not piatto:
        raise HTTPException(status_code=404, detail=f"Piatto {dettaglio.piatto_id} non trovato")
    
    db.add(DettaglioOrdine(
        ordine_id=nuovo_ordine.ordine_id,
        piatto_id=dettaglio.piatto_id,
        quantita=dettaglio.quantita
        )
    )
    db.commit()
    db.refresh(nuovo_ordine)
    return nuovo_ordine