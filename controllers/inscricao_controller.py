from services.inscricao_service import InscricaoService

class InscricaoController:
    #método construtor
    def __init__(self):
        self.servico = InscricaoService()

    #controler listar
    def listar(self, db):
        return self.servico.listar(db)

    #controler listar_id
    def listar_id(self, db, pessoa_id, corrida_idcorrida):
        return self.servico.listar_id(db, pessoa_id, corrida_idcorrida)

    #controle cadastrar
    def cadastrar(self, db, inscricao):
        return self.servico.cadastrar(db, inscricao)

    # controller alterar inscricao
    def alterar(self, db, pessoa_id, corrida_idcorrida, inscricao):
        return self.servico.alterar(
            db,
            pessoa_id,
            corrida_idcorrida,
            inscricao
        )

    # controller excluir inscricao
    def excluir(self, db, pessoa_id, corrida_idcorrida):
        return self.servico.excluir(
            db,
            pessoa_id,
            corrida_idcorrida
        )