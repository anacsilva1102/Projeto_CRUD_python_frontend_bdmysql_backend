from repositories.corrida_repository import CorridaRepository

class CorridaService:
    #método contrutor
    def __init__(self):
        self.repo = CorridaRepository()

    #serviço listar
    def listar(self, db):
        return self.repo.listar(db)

    #serviço listar_id
    def listar_id(self, db, id):
        return self.repo.corrida_id(db, id)
    
    #serviço cadastrar
    def cadastrar(self, db, corrida):
        return self.repo.cadastar(db, corrida)

    # serviço alterar
    def alterar(self, db, id, corrida):
        return self.repo.alterar(db, id, corrida)

    # serviço excluir
    def excluir(self, db, id):
        return self.repo.excluir(db, id)