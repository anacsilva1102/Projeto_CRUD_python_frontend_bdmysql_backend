from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.pessoa_route import router as pessoa_router
from routes.corrida_route import router as corrida_router
from routes.inscricao_route import router as inscricao_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://127.0.0.1:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pessoa_router)
app.include_router(corrida_router)
app.include_router(inscricao_router)


"""
    PARA EXECUTAR O PROJETO DIGITE A LINHA DE COMANDO:

    uvicorn main:app --reload

    python -m uvicorn main:app --reload
"""