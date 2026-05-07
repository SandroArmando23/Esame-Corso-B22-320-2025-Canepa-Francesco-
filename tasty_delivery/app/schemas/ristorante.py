from pydantic import BaseModel, Field
from typing import Optional
from schemas.tipologia import Tipologia


class RistoranteBase(BaseModel):
    nome: str = Field(min_length=1, max_length=80)
    telefono: Optional[str] = None


class RistoranteCreate(RistoranteBase):
    tipologia_id: int

class Ristorante(RistoranteBase):
    ristorante_id: int
    tipologia: Tipologia

    class Config:
        from_attributes=True