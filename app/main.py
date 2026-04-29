from fastapi import FastAPI
from app.database import Base, engine
from app.models import cliente_model

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def inicio():
    return {"mensagem": "API da gráfica funcionando"}