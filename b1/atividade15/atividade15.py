from PIL import ImageSequence
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/tarefas"


st.set_page_config(page_title="Lista de tarefas", layout="centered")

st.title("Lista de tarefas")
st.divider()

def limpar_inputs():
    st.session_state["limpar_campos"] = True


try:
    res = requests.get(API_URL)
    tarefas = res.json() if res.status_code == 200 else []
except Exception:
    st.error("Não foi possível conectar à API")
    tarefas = []

icones_status = {"To do": "🟡 To do", "Doing": "🔵 Doing", "Done": "🟢 Done"}

if tarefas:
    dados_tabela = [
        {
            "Id": t["id"],
            "Tarefa": t["descricao"],
            "Status": icones_status[t["status"]]
        }
        for t in tarefas
    ]
    st.dataframe(dados_tabela, use_container_width=True, hide_index=True)
else:
    st.info("Nenhuma tarefa cadastrada.")

st.divider()

if st.session_state.get("limpar_campos"):
    st.session_state["input_id"] = 0
    st.session_state["input_descricao"] = ""
    st.session_state["input_status"] = ""
    st.session_state["limpar_campos"] = False

coluna_id, coluna_descricao, coluna_status = st.columns([1, 2, 1.2])

with coluna_id:
    input_id = st.number_input("Id (editar|excluir)", min_value= 0, step=1, key="input_id")

with coluna_descricao:
    input_descricao = st.text_input("Descrição", key="input_descricao")

with coluna_status:
    input_status = st.selectbox("Status", ["", "🟡 To do", "🔵 Doing", "🟢 Done"], key="input_status")


coluna_nova, coluna_edita, coluna_exclui = st.columns(3)

with coluna_nova:
    if(st.button("Nova tarefa", use_container_width=True)):
        if not input_descricao.strip():
           st.warning("A descrição é obrigatória!")
        else:
            payload = {
                "descricao": input_descricao.strip(),
                "status": next((k for k, v in icones_status.items() if v == input_status.strip()), "To do")
            }
            r = requests.post(API_URL, json=payload)

            if(r.status_code == 200):
                st.success("Tarefa adicionada com sucesso!")
                limpar_inputs()
                st.rerun()
            else:
                st.error("Erro ao adicionar tarefa.")

with coluna_edita:
    if(st.button("Editar", use_container_width=True)):
        if(input_id <= 0):
            st.warning("Id precisa ser maior que 0.")
        else:
            payload = {}

            if input_descricao.strip():
                payload["descricao"] = input_descricao.strip()
            if input_status.strip():
                payload["status"] = next((k for k, v in icones_status.items() if v == input_status.strip()), "To do")
            
            r = requests.put(f"{API_URL}/{input_id}", json=payload)

            if(r.status_code == 200):
                st.success(f"Tarefa {input_id} editada com sucesso!")
                limpar_inputs()
                st.rerun()
            else:
                st.error("Tarefa não encontrada.")
    
with coluna_exclui:
    if(st.button("Excluir", use_container_width=True)):
        if(input_id <= 0):
            st.warning("Id precisa ser maior que 0")
        else:
            r = requests.delete(f"{API_URL}/{input_id}")

            if(r.status_code == 200):
                st.success("Tarefa excluída com sucesso!")
                limpar_inputs()
                st.rerun()
            else:
                st.error("Tarefa não encontrada")