from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from tasty_delivery.database import Base
from sqlalchemy.orm import relationship

class Ristorante(Base):
    __tablename__ = "ristoranti"
    
    ristorante_id = Column(Integer, primary_key=True, index=True, auto_increment=True)
    nome = Column(String(100), unique=True, index=True, nullable=False)
    telefono = Column(String(20), index=True, nullable=True)
    
    tipologia_id=Column(Integer, ForeignKey("tipologie.tipologia_id"))
    
    tipologia = relationship("Tipologia", back_populates="ristorante")
    piatto = relationship("Piatto", back_populates="ristorante", cascade="all, delete-orphan")
    ordine = relationship("Ordine", back_populates="ristorante")
    
