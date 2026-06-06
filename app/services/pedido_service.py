from sqlalchemy.orm import Session

from app.models.pedido_model import (
    Pedido,
    ItemPedido
)

from app.models.cliente_model import Cliente

from app.services.email_service import (
    enviar_email_pedido
)

import asyncio


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

    # ==========================
    # BUSCA CLIENTE
    # ==========================

    cliente = db.query(Cliente).filter(
        Cliente.id == dados_pedido.cliente_id
    ).first()

    # ==========================
    # ENVIO DE EMAIL
    # ==========================

    if cliente:

        itens_texto = ""

        for item in dados_pedido.itens:

            itens_texto += (
                f"Produto ID: {item.produto_id}\n"
                f"Quantidade: {item.quantidade}\n"
                f"Valor Unitário: R$ {item.valor_unitario}\n"
                f"Subtotal: R$ {item.subtotal}\n"
                f"Observações: {item.observacoes}\n\n"
            )

        corpo_email = f"""
NOVO PEDIDO RECEBIDO

Pedido: #{novo_pedido.id}

Cliente: {cliente.nome}

Telefone: {cliente.telefone}

Email: {cliente.email or "Não informado"}

Tipo de Entrega: {cliente.tipo_entrega if hasattr(cliente, 'tipo_entrega') else 'Não informado'}

Endereço:
{cliente.endereco if hasattr(cliente, 'endereco') else 'Não informado'}

--------------------------------------

ITENS DO PEDIDO

{itens_texto}

--------------------------------------

TOTAL: R$ {novo_pedido.valor_total}
"""

        try:

            asyncio.run(
                enviar_email_pedido(
                    assunto=f"Novo Pedido #{novo_pedido.id}",
                    destinatario="pedidos.graficapergaminho@gmail.com",
                    corpo=corpo_email,
                )
            )

        except Exception as e:

            print(f"Erro ao enviar email: {e}")

    return novo_pedido


def listar_pedidos(db: Session):
    return db.query(Pedido).all()


def buscar_pedido_por_id(
    db: Session,
    pedido_id: int
):
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