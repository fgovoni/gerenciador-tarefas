from fastapi.testclient import TestClient
from fastapi import status
from gerenciador_tarefas import app

def test_quando_listar_tarefas_devo_ter_como_retornor_codigo_de_status_200():
	cliente = TestClient(app)
	resposta = client.get("/tarefas")
	assert respostas.status_code == status.HTTP_200_OK
