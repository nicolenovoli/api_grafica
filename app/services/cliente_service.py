from sqlalchemy.orm import Session
from app.models.cliente_model import Cliente
from app.schemas.cliente_schema import ClienteCreate


def cadastrar_cliente(db: Session, cliente: ClienteCreate):
    novo_cliente = Cliente(
        nome=cliente.nome,
        telefone=cliente.telefone,
        email=cliente.email,
        tipo_entrega=cliente.tipo_entrega.value,
        endereco=cliente.endereco,
    )

    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return novo_cliente