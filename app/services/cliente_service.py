from sqlalchemy.orm import Session

from app.models.cliente_model import Cliente
from app.schemas.cliente_schema import ClienteCreate


def cadastrar_cliente(
    db: Session,
    cliente: ClienteCreate
):

    cliente_existente = db.query(
        Cliente
    ).filter(
        Cliente.telefone == cliente.telefone
    ).first()

    # =====================================
    # CLIENTE JÁ EXISTE
    # =====================================

    if cliente_existente:

        cliente_existente.nome = cliente.nome

        cliente_existente.email = cliente.email

        cliente_existente.tipo_entrega = (
            cliente.tipo_entrega
        )

        cliente_existente.endereco = (
            cliente.endereco
        )

        db.commit()

        db.refresh(cliente_existente)

        return cliente_existente

    # =====================================
    # NOVO CLIENTE
    # =====================================

    novo_cliente = Cliente(

        nome=cliente.nome,

        telefone=cliente.telefone,

        email=cliente.email,

        tipo_entrega=cliente.tipo_entrega,

        endereco=cliente.endereco,
    )

    db.add(novo_cliente)

    db.commit()

    db.refresh(novo_cliente)

    return novo_cliente


def listar_clientes(
    db: Session
):
    return db.query(
        Cliente
    ).all()


def buscar_cliente_por_telefone(
    db: Session,
    telefone: str
):
    return db.query(
        Cliente
    ).filter(
        Cliente.telefone == telefone
    ).first()