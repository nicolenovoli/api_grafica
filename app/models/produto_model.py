from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
)

from sqlalchemy.orm import relationship

from app.database import Base


class Produto(Base):

    __tablename__ = "produtos"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    nome = Column(
        String,
        nullable=False,
    )

    descricao = Column(
        String,
        nullable=False,
    )

    preco_base = Column(
        Float,
        nullable=False,
    )

    opcoes = relationship(
        "ProdutoOpcao",
        back_populates="produto",
    )