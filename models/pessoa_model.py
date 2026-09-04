from sqlalchemy import Column, Integer, String, DECIMAL, Date
from database import Base


class Pessoa(Base):
    __tablename__ = "pessoa"

    idpessoa = Column(Integer, primary_key=True, index=True)
    nome = Column(String(60))
    sexo = Column(String(1))
    datanascimento = Column(Date)
    idade = Column(Integer)
    peso = Column(Integer)
    altura = Column(DECIMAL(10, 2))
    imc = Column(DECIMAL(10, 2))
    cpf = Column(String(14))
    cep = Column(String(9))
    rua = Column(String(100))
    bairro = Column(String(100))
    cidade = Column(String(100))
    uf = Column(String(2))