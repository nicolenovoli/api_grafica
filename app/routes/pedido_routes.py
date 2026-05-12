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
    buscar_pedido_por_id,
    buscar_pedidos_por_telefone
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
    """Cria um novo pedido"""
    return criar_pedido(db, pedido)


@router.get("/", response_model=list[PedidoResponse])
def buscar_pedidos(
    db: Session = Depends(get_db)
):
    """Busca todos os pedidos disponíveis"""
    return listar_pedidos(db)


@router.get("/{pedido_id}", response_model=PedidoResponse)
def buscar_pedido(
    pedido_id: int,
    db: Session = Depends(get_db)
):
    """Busca um pedido por ID"""
    pedido = buscar_pedido_por_id(db, pedido_id)

    if pedido is None:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    return pedido

@router.get(
    "/cliente/{telefone}",
    response_model=list[PedidoResponse]
)
def buscar_pedidos_cliente(
    telefone: str,
    db: Session = Depends(get_db)
):
    """Busca os pedidos por telefone"""
    return buscar_pedidos_por_telefone(
        db,
        telefone
    )