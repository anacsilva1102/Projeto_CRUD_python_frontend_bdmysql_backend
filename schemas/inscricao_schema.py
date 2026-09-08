from pydantic import BaseModel

class InscricaoSchema(BaseModel):

    pessoa_id: int

    corrida_idcorrida: int

    tamanho_camisa: str