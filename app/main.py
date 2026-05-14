from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from app.database import (
    Base,
    engine,
    SessionLocal
)

from app.models import (
    cliente_model,
    produto_model,
    pedido_model,
    produto_opcao_model
)

from app.routes import (
    cliente_routes,
    produto_routes,
    pedido_routes
)

from app.seed import (
    criar_produtos_iniciais
)

app = FastAPI(title="API Gráfica")

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

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
app.include_router(pedido_routes.router)


@app.get("/")
def inicio():

    return {
        "mensagem":
            "API da gráfica funcionando"
    }