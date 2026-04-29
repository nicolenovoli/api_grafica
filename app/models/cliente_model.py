from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    endereco = Column(String, nullable=False)
    ativo = Column(Boolean, default=True)