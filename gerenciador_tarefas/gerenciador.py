from fastapi import FastAPI

TAREFAS = []

app = FastAPI()

@app.get("/tarefas")
def listar():
    return TAREFAS