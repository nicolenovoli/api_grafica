from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.cliente_schema import ClienteCreate, ClienteResponse
from app.services.cliente_service import cadastrar_cliente, buscar_cliente_por_telefone


router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router.post("/", response_model=ClienteResponse)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    """Cria um novo cliente"""
    return cadastrar_cliente(db, cliente)

@router.get(
    "/telefone/{telefone}",
    response_model=ClienteResponse
)
def buscar_cliente_telefone(
    telefone: str,
    db: Session = Depends(get_db)
):
    """Busca um cliente por telefone"""
    cliente = buscar_cliente_por_telefone(
        db,
        telefone
    )

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    return cliente