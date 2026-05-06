from pydantic import BaseModel, EmailStr, field_validator, model_validator
from typing import Optional


class ClienteCreate(BaseModel):
    nome: str
    telefone: str
    email: Optional[EmailStr] = None
    tipo_entrega: str
    endereco: Optional[str] = None

    @field_validator("nome", "telefone", "tipo_entrega")
    @classmethod
    def campo_obrigatorio(cls, valor):
        if not valor or not valor.strip():
            raise ValueError("Campo obrigatório")
        return valor

    @field_validator("tipo_entrega")
    @classmethod
    def validar_tipo_entrega(cls, valor):
        valor = valor.lower().strip()

        if valor not in ["entrega", "retirada"]:
            raise ValueError("O tipo de entrega deve ser 'entrega' ou 'retirada'")

        return valor

    @model_validator(mode="after")
    def validar_endereco_se_entrega(self):
        if self.tipo_entrega == "entrega":
            if not self.endereco or not self.endereco.strip():
                raise ValueError("Endereço é obrigatório quando o tipo de entrega for 'entrega'")
        return self


class ClienteResponse(BaseModel):
    id: int
    nome: str
    telefone: str
    email: Optional[EmailStr] = None
    tipo_entrega: str
    endereco: Optional[str] = None

    class Config:
        from_attributes = True