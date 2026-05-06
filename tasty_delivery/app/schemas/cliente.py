from pydantic import BaseModel, Field

class ClienteBase(BaseModel):
    nome: str 
    email: str = Field(min_length=1, max_lenght=80)
    indirizzo: str = Field(min_length=1, max_lenght=80)

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    cliente_id: int

    class Config:
        from_attributes=True