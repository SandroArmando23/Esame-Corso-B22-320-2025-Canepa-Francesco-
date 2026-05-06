from pydantic import BaseModel, Field


class DettaglioOrdineBase(BaseModel):
    piatto_id: int
    quantita: int = Field(gt=0)  # > di 0

class DettaglioOrdineCreate(DettaglioOrdineBase):
    dettaglio_ordine_id: int

class DettaglioOrdine(DettaglioOrdineBase):
    ordine_id: int
    piatto_id: int
    quantita: int = Field(gt=0)

    class Config:
        from_attributes=True