from pydantic import BaseModel


class TipologiaBase(BaseModel):
    nome: str

class TipologiaCreate(TipologiaBase):
    pass

class Tipologia(TipologiaBase):
    tipologia_id: int
    
    class Config:
        from_attributes=True