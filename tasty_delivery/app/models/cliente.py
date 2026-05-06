from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.orm import relationship



class Cliente(Base):
    __tablename__ = "clienti"

    cliente_id = Column(Integer, primary_key=True, index=True, auto_increment=True)
    nome = Column(String(100),index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    indirizzo = Column(String(255), index=True, nullable=False)
    
    ordine = relationship("Ordine", back_populates="cliente")
