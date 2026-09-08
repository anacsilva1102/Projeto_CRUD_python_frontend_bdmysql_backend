from repositories.inscricao_repository import InscricaoRepository

class InscricaoService:
    #método contrutor
    def __init__(self):
        self.repo = InscricaoRepository()

    #serviço listar
    def listar(self, db):
        return self.repo.listar(db)

    #serviço listar_id
    def listar_id(self, db, pessoa_id, corrida_idcorrida):
        return self.repo.inscricao_id(db, pessoa_id, corrida_idcorrida)

    #serviço cadastrar
    def cadastrar(self, db, inscricao):
        return self.repo.cadastar(db, inscricao)

    # serviço alterar
    def alterar(self, db, pessoa_id, corrida_idcorrida, inscricao):
        return self.repo.alterar(db, pessoa_id, corrida_idcorrida, inscricao)

    # serviço excluir
    def excluir(self, db, pessoa_id, corrida_idcorrida):
        return self.repo.excluir(db, pessoa_id, corrida_idcorrida)