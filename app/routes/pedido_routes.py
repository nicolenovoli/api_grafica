from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.pedido_schema import (
    PedidoCreate,
    PedidoResponse
)

from app.services.pedido_service import (
    criar_pedido,
    listar_pedidos,
    buscar_pedido_por_id
)

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)


@router.post("/", response_model=PedidoResponse)
def cadastrar_pedido(
    pedido: PedidoCreate,
    db: Session = Depends(get_db)
):
    return criar_pedido(db, pedido)


@router.get("/", response_model=list[PedidoResponse])
def buscar_pedidos(
    db: Session = Depends(get_db)
):
    return listar_pedidos(db)


@router.get("/{pedido_id}", response_model=PedidoResponse)
def buscar_pedido(
    pedido_id: int,
    db: Session = Depends(get_db)
):
    pedido = buscar_pedido_por_id(db, pedido_id)

    if pedido is None:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    return pedido