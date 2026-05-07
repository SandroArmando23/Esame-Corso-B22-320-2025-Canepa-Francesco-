from pydantic import BaseModel, Field


class DettaglioOrdineBase(BaseModel):
    piatto_id: int
    quantita: int = Field(gt=0)  # > di 0

class DettaglioOrdineCreate(DettaglioOrdineBase):
    pass

class DettaglioOrdine(DettaglioOrdineBase):
    dettaglio_ordine_id: int
    ordine_id: int

    class Config:
        from_attributes=True