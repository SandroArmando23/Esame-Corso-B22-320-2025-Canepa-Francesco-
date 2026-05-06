from pydantic import BaseModel
from typing import List
from datetime import datetime
from schemas.dettaglio_ordine import DettaglioOrdineCreate, DettaglioOrdine

class OrdineBase(BaseModel):
    cliente_id: int
    ristorante_id: int

class OrdineCreate(OrdineBase):
    dettagli: List[DettaglioOrdineCreate]

class Ordine(OrdineBase):
    ordine_id: int
    data_ora: datetime
    stato: str
    dettagli: List[DettaglioOrdine] = []

    class Config:
        from_attributes=True