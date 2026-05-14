from pydantic import BaseModel


class ProdutoOpcaoResponse(BaseModel):

    id: int

    grupo: str

    nome: str

    valor_adicional: float

    class Config:

        from_attributes = True