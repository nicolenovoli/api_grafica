from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class ItemPedidoCreate(BaseModel):
    produto_id: int
    nome_produto: str
    quantidade: int
    valor_unitario: float
    subtotal: float
    observacoes: Optional[str] = None


class PedidoCreate(BaseModel):
    cliente_id: int
    valor_total: float
    itens: List[ItemPedidoCreate]


class ItemPedidoResponse(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    valor_unitario: float
    subtotal: float
    observacoes: Optional[str] = None

    class Config:
        from_attributes = True


class PedidoResponse(BaseModel):
    id: int
    cliente_id: int
    valor_total: float
    status: str
    data_pedido: datetime

    itens: List[ItemPedidoResponse]

    class Config:
        from_attributes = True