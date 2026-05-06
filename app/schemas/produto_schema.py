from pydantic import BaseModel
from typing import Optional


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    imagem: Optional[str] = None

    class Config:
        from_attributes = True