from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database import Base


class ProdutoOpcao(Base):

    __tablename__ = "produto_opcoes"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    produto_id = Column(
        Integer,
        ForeignKey("produtos.id"),
        nullable=False,
    )

    grupo = Column(
        String,
        nullable=False,
    )

    nome = Column(
        String,
        nullable=False,
    )

    valor_adicional = Column(
        Float,
        default=0,
    )

    produto = relationship(
        "Produto",
        back_populates="opcoes",
    )