from enum import Enum
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel, constr

app = FastAPI()


class EstadosPossiveis(str, Enum):
    finalizado = "finalizado"
    nao_finalizado = "não finalizado"


class TarefaEntrada(BaseModel):
    titulo: constr(min_length=3, max_length=50)
    descricao: constr(max_length=140)
    estado: EstadosPossiveis = EstadosPossiveis.nao_finalizado


class Tarefa(TarefaEntrada):
    id: UUID


TAREFAS = []


@app.get("/tarefas")
def listar():
    return TAREFAS


@app.post(
    "/tarefas", response_model=Tarefa, status_code=status.HTTP_201_CREATED
)
def criar(tarefa: TarefaEntrada):
    nova_tarefa = tarefa.dict()
    nova_tarefa.update({"id": uuid4()})
    TAREFAS.append(nova_tarefa)
    return nova_tarefa


@app.put("/tarefas/{id}", response_model=Tarefa)
def atualizar(id: UUID, tarefa: TarefaEntrada):
    for tarefa_atual in TAREFAS:
        if tarefa_atual["id"] == id:
            tarefa_atual.update(tarefa.dict())
            return tarefa_atual
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.delete("/tarefas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar(id: UUID):
    for tarefa in TAREFAS:
        if tarefa["id"] == id:
            TAREFAS.remove(tarefa)
            return tarefa
    return {"erro": "Tarefa não encontrada"}