from pydantic import BaseModel

from typing import List

from app.schemas.produto_opcao_schema import (
    ProdutoOpcaoResponse
)


class ProdutoResponse(BaseModel):

    id: int

    nome: str

    descricao: str

    preco_base: float

    opcoes: List[
        ProdutoOpcaoResponse
    ] = []

    class Config:

        from_attributes = True