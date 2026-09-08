from sqlalchemy import Column, Integer, String

from database import Base

class Inscricao(Base):
    __tablename__ = "inscricao"

    pessoa_id = Column(Integer, primary_key=True, index=True)
    corrida_idcorrida = Column(Integer, primary_key=True, index=True)
    tamanho_camisa = Column(String(1))