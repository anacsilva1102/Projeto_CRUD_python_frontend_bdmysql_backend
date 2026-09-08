from fastapi import APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal

from controllers.inscricao_controller import InscricaoController
from schemas.inscricao_schema import InscricaoSchema

router = APIRouter(
    prefix="/inscricao",
    tags=["Inscrição"]
)

controller = InscricaoController()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar():
    db = next(get_db())

    return controller.listar(db)

@router.get("/{pessoa_id}/{corrida_idcorrida}")
def listar_id(pessoa_id: int, corrida_idcorrida: int):
    db = next(get_db())

    return controller.listar_id(
        db,
        pessoa_id,
        corrida_idcorrida
    )

@router.post("/")
def cadstrar(inscricao: InscricaoSchema):
    db = next(get_db())

    return controller.cadastrar(db, inscricao)

@router.put("/{pessoa_id}/{corrida_idcorrida}")
def alterar(
    pessoa_id: int,
    corrida_idcorrida: int,
    inscricao: InscricaoSchema
):

    db = next(get_db())

    return controller.alterar(
        db,
        pessoa_id,
        corrida_idcorrida,
        inscricao
    )

@router.delete("/{pessoa_id}/{corrida_idcorrida}")
def excluir(pessoa_id: int, corrida_idcorrida: int):

    db = next(get_db())

    return controller.excluir(
        db,
        pessoa_id,
        corrida_idcorrida
    )