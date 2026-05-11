from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime

from app.database import Base


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)

    cliente_id = Column(
        Integer,
        ForeignKey("clientes.id"),
        nullable=False
    )

    valor_total = Column(Float, nullable=False)

    status = Column(
        String,
        default="aguardando pagamento"
    )

    data_pedido = Column(
        DateTime,
        default=datetime.utcnow
    )

    cliente = relationship("Cliente")

    itens = relationship(
        "ItemPedido",
        back_populates="pedido",
        cascade="all, delete-orphan"
    )


class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column(Integer, primary_key=True, index=True)

    pedido_id = Column(
        Integer,
        ForeignKey("pedidos.id"),
        nullable=False
    )

    produto_id = Column(
        Integer,
        ForeignKey("produtos.id"),
        nullable=False
    )

    quantidade = Column(Integer, nullable=False)

    valor_unitario = Column(Float, nullable=False)

    subtotal = Column(Float, nullable=False)

    observacoes = Column(String, nullable=True)

    pedido = relationship(
        "Pedido",
        back_populates="itens"
    )

    produto = relationship("Produto")