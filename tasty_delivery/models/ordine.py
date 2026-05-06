from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from tasty_delivery.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class Ordine(Base):
    __tablename__ = "ordini"
    
    ordine_id = Column(Integer, primary_key=True, index=True, auto_increment=True)
    data_ora = Column(DateTime, deafault=datetime.now())   # ricorda potrebbe dare problemi a runtime se mai commenta
    stato = Column(String(50), default="In preparazione")  # ricorda di commentare che c'è solo stato di default
    
    cliente_id = Column(Integer, ForeignKey("clienti.cliente_id"), nullable=False)
    ristorante_id = Column(Integer, ForeignKey("ristoranti.ristorante_id"), nullable=False)
    
    cliente = relationship("Cliente", back_populates="ordini")
    ristorante = relationship("Ristorante", back_populates="ordini")
    dettagli = relationship("DettaglioOrdine", back_populates="ordine", cascade="all, delete-orphan")
    