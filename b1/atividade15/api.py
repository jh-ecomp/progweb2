import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
LISTA_TAREFAS = "tarefas.json"

class Tarefa(BaseModel):
    descricao: str
    status: str = "To do"

class EditaTarefa(BaseModel):
    descricao: str | None = None
    status: str | None = None

def carregar_tarefas() -> list:
    if not os.path.exists(LISTA_TAREFAS):
        return []

    with open(LISTA_TAREFAS, "r", encoding="utf-8") as lista:
        try:
            return json.load(lista)
        except json.JSONDecodeError:
            return []


def salvar_tarefas(tarefas: list):
    with open(LISTA_TAREFAS, "w", encoding="utf-8") as lista:
        json.dump(tarefas, lista, indent=4, ensure_ascii=False)


@app.get("/tarefas")
def listar_tarefas():
    return carregar_tarefas()


@app.post("/tarefas")
def cria_tarefa(tarefa: Tarefa):
    tarefas = carregar_tarefas()
    novo_id = max([t["id"] for t in tarefas], default=0) + 1

    nova_tarefa = {
        "id": novo_id,
        "descricao": tarefa.descricao,
        "status": tarefa.status
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    return nova_tarefa


@app.put("/tarefas/{id}")
def edita_tarefa(id: int, dados: EditaTarefa):
    tarefas = carregar_tarefas()

    for t in tarefas:
        if(t["id"] == id):
            if dados.descricao and dados.descricao.strip():
                t["descricao"] = dados.descricao.strip()
            if dados.status and dados.status.strip():
                t["status"] = dados.status.strip()
            salvar_tarefas(tarefas)
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.delete("/tarefas/{id}")
def excluir_tarefa(id: int):
    tarefas = carregar_tarefas()

    tarefas_limpas = [t for t in tarefas if t["id"] != id]

    if(len(tarefas_limpas) == len(tarefas)):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    salvar_tarefas(tarefas_limpas)
    return {"mensagem": "Tarefa escluída com sucesso"}