from pydantic import BaseModel
from datetime import date


class PessoaSchema(BaseModel):
    nome: str
    sexo: str
    datanascimento: date
    peso: int
    altura: float