from fastapi import FastAPI

from app.database import Base, engine, SessionLocal

from app.models import (
    cliente_model,
    produto_model
)

from app.routes import (
    cliente_routes,
    produto_routes
)

from app.seed import criar_produtos_iniciais


app = FastAPI(title="API Gráfica")

Base.metadata.create_all(bind=engine)


def iniciar_dados():
    db = SessionLocal()

    try:
        criar_produtos_iniciais(db)
    finally:
        db.close()


iniciar_dados()

app.include_router(cliente_routes.router)
app.include_router(produto_routes.router)


@app.get("/")
def inicio():
    return {"mensagem": "API da gráfica funcionando"}