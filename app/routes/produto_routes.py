from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.produto_schema import ProdutoResponse
from app.services.produto_service import listar_produtos, buscar_produto_por_id


router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)


@router.get("/", response_model=list[ProdutoResponse])
def buscar_produtos(db: Session = Depends(get_db)):
    """Busca todos os produtos disponíveis"""
    return listar_produtos(db)


@router.get("/{produto_id}", response_model=ProdutoResponse)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    """Busca os produtos por ID"""
    produto = buscar_produto_por_id(db, produto_id)

    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return produto