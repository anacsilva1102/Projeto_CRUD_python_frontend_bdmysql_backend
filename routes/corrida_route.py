from fastapi import APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal

from controllers.corrida_controller import CorridaController
from schemas.corrida_schema import CorridaSchema

router = APIRouter(
    prefix="/corrida",
    tags=["Corrida"]
)

controller = CorridaController()

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

@router.get("/{id}")
def listar_id(id: int):
    db = next(get_db())

    return controller.listar_id(db, id)

@router.post("/")
def cadstrar(corrida: CorridaSchema):
    db = next(get_db())
    return controller.cadastrar(db, corrida)

@router.put("/{id}")
def alterar(id: int, corrida: CorridaSchema):

    db = next(get_db())

    return controller.alterar(
        db,
        id,
        corrida
    )

@router.delete("/{id}")
def excluir(id: int):

    db = next(get_db())

    return controller.excluir(
        db,
        id
    )