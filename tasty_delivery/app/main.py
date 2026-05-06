from fastapi import FastAPI
from database import engine, Base
from routers import ordine
from routers import piatto, ristorante, tipologia


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TastyDelivery",
    description="API per gestione Delivery per la prova d'esame",
    version="1.0.0"
)

app.include_router(ristorante.router)
app.include_router(tipologia.router)
app.include_router(piatto.router)
app.include_router(ordine.router)


@app.get("/")
def root():
    return {"message": "Benvenuto in TastyDelivery"}