from sqlalchemy.orm import Session

from app.models.pedido_model import (
    Pedido,
    ItemPedido
)

from app.models.cliente_model import Cliente


def criar_pedido(db: Session, dados_pedido):
    novo_pedido = Pedido(
        cliente_id=dados_pedido.cliente_id,
        valor_total=dados_pedido.valor_total
    )

    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)

    for item in dados_pedido.itens:
        novo_item = ItemPedido(
            pedido_id=novo_pedido.id,
            produto_id=item.produto_id,
            quantidade=item.quantidade,
            valor_unitario=item.valor_unitario,
            subtotal=item.subtotal,
            observacoes=item.observacoes
        )

        db.add(novo_item)

    db.commit()
    db.refresh(novo_pedido)

    return novo_pedido


def listar_pedidos(db: Session):
    return db.query(Pedido).all()


def buscar_pedido_por_id(db: Session, pedido_id: int):
    return db.query(Pedido).filter(
        Pedido.id == pedido_id
    ).first()

def buscar_pedidos_por_telefone(
    db: Session,
    telefone: str
):
    cliente = db.query(Cliente).filter(
        Cliente.telefone == telefone
    ).first()

    if cliente is None:
        return []

    return db.query(Pedido).filter(
        Pedido.cliente_id == cliente.id
    ).all()