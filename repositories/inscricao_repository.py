from sqlalchemy.orm import Session
from models.inscricao_model import Inscricao

class InscricaoRepository:

    #listar todas as inscrições
    def listar(self, db: Session):
        return db.query(Inscricao).all()

    #cadastro Inscrição
    def cadastar(self, db: Session, inscricao):
        nova_inscricao = Inscricao(
            pessoa_id=inscricao.pessoa_id,
            corrida_idcorrida=inscricao.corrida_idcorrida,
            tamanho_camisa=inscricao.tamanho_camisa
        )

        db.add(nova_inscricao)
        db.commit()
        db.refresh(nova_inscricao)

        return nova_inscricao

    #listar inscrição por id
    def inscricao_id(self, db: Session, pessoa_id: int, corrida_idcorrida: int):
        return db.query(Inscricao).filter(
            Inscricao.pessoa_id == pessoa_id,
            Inscricao.corrida_idcorrida == corrida_idcorrida
        ).first()

    #alterar inscrição
    def alterar(self, db: Session, pessoa_id: int, corrida_idcorrida: int, inscricao):
        inscricao_bd = self.inscricao_id(db, pessoa_id, corrida_idcorrida)

        if inscricao_bd is None:
            return {"Mensagem": "Inscrição não encontrada"}

        inscricao_bd.tamanho_camisa = inscricao.tamanho_camisa

        db.commit()
        db.refresh(inscricao_bd)

        return inscricao_bd

    #excluir inscrição
    def excluir(self, db: Session, pessoa_id: int, corrida_idcorrida: int):
        inscricao_bd = self.inscricao_id(db, pessoa_id, corrida_idcorrida)

        if inscricao_bd is None:
            return {"Mensagem": "Inscrição não encontrada"}

        db.delete(inscricao_bd)
        db.commit()

        return {"Mensagem": "Inscrição Excluída com Sucesso!!"}