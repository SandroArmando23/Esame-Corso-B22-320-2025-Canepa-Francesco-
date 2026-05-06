from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from tasty_delivery.database import Base
from sqlalchemy.orm import relationship


class DettaglioOrdine(Base):
    __tablename__ = "dettagli_ordine"
    
    dettaglio_ordine_id = Column(Integer, primary_key=True, auto_increment=True, index=True)
    quantita = Column(Integer, nullable=False, default=1)
    
    
    ordine_id = Column(Integer, ForeignKey("ordini.ordine_id"), nullable=False)
    piatto_id = Column(Integer, ForeignKey("piatti.piatto_id"), nullable=False)
    
    
    ordine = relationship("Ordine", back_populates="dettagli")
    piatto = relationship("Piatto", back_populates="dettaglio_ordine")
