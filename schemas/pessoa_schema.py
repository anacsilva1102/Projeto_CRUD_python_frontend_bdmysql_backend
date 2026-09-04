from pydantic import BaseModel
from datetime import date

class PessoaSchema(BaseModel):
    nome: str
    sexo: str
    datanascimento: date
    idade: int
    peso: float
    altura: float
    imc: float = 0
    cpf: str = ''
    cep: str = ''
    rua: str = ''
    bairro: str = ''
    cidade: str = ''
    uf: str = ''