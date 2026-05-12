from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=True)
    tipo_entrega = Column(String, nullable=False)
    endereco = Column(String, nullable=True)