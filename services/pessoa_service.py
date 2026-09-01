from repositories.pessoa_repository import PessoaRepository

class PessoaService:
    #método contrutor
    def __init__(self):
        self.repo = PessoaRepository()

    #serviço listar
    def listar(self, db):
        return self.repo.listar(db)

    #serviço listar_id
    def listar_id(self, db, id):
        return self.repo.pessoa_id(db, id)
    
    #serviço cadastrar
    def cadastrar(self, db, pessoa):
        return self.repo.cadastar(db, pessoa)

    # serviço alterar
    def alterar(self, db, id, pessoa):
        return self.repo.alterar(db, id, pessoa)


    # serviço excluir
    def excluir(self, db, id):
        return self.repo.excluir(db, id)
