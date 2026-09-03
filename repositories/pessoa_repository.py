from sqlalchemy.orm import Session
from models.pessoa_model import Pessoa

class PessoaRepository:

    def listar(self, db: Session):
        pessoas = db.query(Pessoa).all()

        for pessoa in pessoas:
            if pessoa.peso and pessoa.altura and float(pessoa.altura) > 0:
                pessoa.imc = round(
                    float(pessoa.peso) / (float(pessoa.altura) * float(pessoa.altura)), 2
                )

        return pessoas

    def cadastar(self, db: Session, pessoa):
        imc = 0

        if pessoa.peso > 0 and pessoa.altura > 0:
            imc = round(
                pessoa.peso / (pessoa.altura * pessoa.altura), 2
            )

        nova_pessoa = Pessoa(
            nome=pessoa.nome,
            sexo=pessoa.sexo,
            datanascimento=pessoa.datanascimento,
            idade=pessoa.idade,
            peso=pessoa.peso,
            altura=pessoa.altura,
            imc=imc,
            cpf=pessoa.cpf,
            cep=pessoa.cep,
            rua=pessoa.rua,
            bairro=pessoa.bairro,
            cidade=pessoa.cidade,
            uf=pessoa.uf
        )

        db.add(nova_pessoa)
        db.commit()
        db.refresh(nova_pessoa)

        return nova_pessoa

    def pessoa_id(self, db: Session, id: int):
        return db.query(Pessoa).filter(Pessoa.idpessoa == id).first()

    def alterar(self, db: Session, id: int, pessoa):
        pessoa_bd = self.pessoa_id(db, id)

        if pessoa_bd is None:
            return {"Mensagem": "Atleta não encontrado"}

        imc = 0

        if pessoa.peso > 0 and pessoa.altura > 0:
            imc = round(
                pessoa.peso / (pessoa.altura * pessoa.altura), 2
            )

        pessoa_bd.nome = pessoa.nome
        pessoa_bd.sexo = pessoa.sexo
        pessoa_bd.datanascimento = pessoa.datanascimento
        pessoa_bd.idade = pessoa.idade
        pessoa_bd.peso = pessoa.peso
        pessoa_bd.altura = pessoa.altura
        pessoa_bd.imc = imc
        pessoa_bd.cpf = pessoa.cpf
        pessoa_bd.cep = pessoa.cep
        pessoa_bd.rua = pessoa.rua
        pessoa_bd.bairro = pessoa.bairro
        pessoa_bd.cidade = pessoa.cidade
        pessoa_bd.uf = pessoa.uf

        db.commit()
        db.refresh(pessoa_bd)

        return pessoa_bd

    def excluir(self, db: Session, id: int):
        pessoa_bd = self.pessoa_id(db, id)

        if pessoa_bd is None:
            return {"Mensagem": "Atleta não encontrado"}

        db.delete(pessoa_bd)
        db.commit()

        return {"Mensagem": "Pessoa Excluída com Sucesso!!"}