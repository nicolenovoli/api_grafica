from fastapi import FastAPI

from app.database import Base, engine
from app.models import cliente_model
from app.routes import cliente_routes


app = FastAPI(title="API Gráfica")

Base.metadata.create_all(bind=engine)

app.include_router(cliente_routes.router)


@app.get("/")
def inicio():
    return {"mensagem": "API da gráfica funcionando"}