from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from tasty_delivery.database import Base
from sqlalchemy.orm import relationship


class Piatto(Base):
    __tablename__ = "piatti"
    
    piatto_id = Column(Integer, primary_key=True, index=True, auto_increment=True)
    nome = Column(String(100), unique=True, index=True, nullable=False)
    prezzo = Column(Float(precision=10, scale=2), nullable=False)
    
    ristorante_id = Column(Integer, ForeignKey("ristoranti.ristorante_id"))
    
    ristorante = relationship("Ristorante", back_populates="piatto")
    dettaglio_ordine = relationship("DettaglioOrdine", back_populates="piatto")
    
    
    