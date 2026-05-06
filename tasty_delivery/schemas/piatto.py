from pydantic import BaseModel
from typing import Optional


class PiattoBase(BaseModel):
    nome: str
    prezzo: float

class PiattoCreate(PiattoBase):
    ristorante_id: int

class Piatto(PiattoBase):
    piatto_id: int
    
    class Config:
        from_attributes=True