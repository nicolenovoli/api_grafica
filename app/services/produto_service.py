from sqlalchemy.orm import Session
from app.models.produto_model import Produto


def listar_produtos(db: Session):
    return db.query(Produto).all()


def buscar_produto_por_id(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()