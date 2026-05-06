from pydantic import BaseModel, Field
from typing import Optional, List
from models.piatto import Piatto
from models.ristorante import Ristorante
from models.ordine import Ordine


class PiattiRistorante(Ristorante):
    piatti: List[Piatto] = []

class OrdineConDettagli(Ordine):
    pass # già include i dettagli


