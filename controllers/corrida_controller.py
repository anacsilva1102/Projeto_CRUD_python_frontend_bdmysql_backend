from services.corrida_service import CorridaService

class CorridaController:
    #método construtor
    def __init__(self):
        self.servico = CorridaService()
    
    #controler listar
    def listar(self, db):
        return self.servico.listar(db)

    #controler listar_id
    def listar_id(self, db, id):
        return self.servico.listar_id(db, id)
    
    #controle cadastrar
    def cadastrar(self, db, corrida):
        return self.servico.cadastrar(db, corrida)

    # controller alterar corrida
    def alterar(self, db, id, corrida):
        return self.servico.alterar(db, id, corrida)

    # controller excluir corrida
    def excluir(self, db, id):
        return self.servico.excluir(db, id)