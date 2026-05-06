from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from tasty_delivery.database import Base


class Tipologia(Base):
    __tablename__ = "tipologie"
    
    tipologia_id = Column(Integer, primary_key=True, index=True, auto_increment=True)
    nome = Column(String(50), unique=True, index=True, nullable=False)
    
    ristorante = relationship("Ristorante", back_populates= "tipologia")