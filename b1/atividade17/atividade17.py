import json
import os
import random
import streamlit as st

ARQUIVO_ALUNOS = os.path.join(os.path.dirname(__file__), "alunos.json")
ALUNOS_PADRAO = ["Ana", "João", "Maria", "Pedro", "Carlos"]


def carregar_alunos() -> list:
    if not os.path.exists(ARQUIVO_ALUNOS):
        salvar_alunos(ALUNOS_PADRAO)
        return list(ALUNOS_PADRAO)

    with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return list(ALUNOS_PADRAO)


def salvar_alunos(alunos: list):
    with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)


st.set_page_config(page_title="Sistema de Sorteio de Alunos", layout="centered")

alunos = carregar_alunos()

if "resultado_sorteio" not in st.session_state:
    st.session_state.resultado_sorteio = None
if "tipo_sorteio" not in st.session_state:
    st.session_state.tipo_sorteio = None

st.title("Sistema de Sorteio de Alunos")
st.markdown("Cadastre nomes de alunos e aperte os botões para sortear e embaralhar.")
st.divider()


if st.button("Embaralhar", use_container_width=True):
    if alunos:
        random.shuffle(alunos)
        salvar_alunos(alunos)
        st.rerun()

st.subheader("Alunos Cadastrados")

if alunos:
    st.write(", ".join(f"`{a}`" for a in alunos))
else:
    st.info("Nenhum aluno cadastrado no momento.")

col_input, col_btn = st.columns([3, 1], vertical_alignment="bottom")

with col_input:
    novo_nome = st.text_input("Novo aluno", placeholder="Digite o nome do aluno...", key="input_novo_nome")

with col_btn:
    if st.button("Cadastrar", use_container_width=True):
        nome_limpo = novo_nome.strip()
        if not nome_limpo:
            st.warning("Informe o nome do aluno!")
        elif nome_limpo in alunos:
            st.warning(f"O aluno '{nome_limpo}' já está cadastrado!")
        else:
            alunos.append(nome_limpo)
            salvar_alunos(alunos)
            st.success(f"Aluno '{nome_limpo}' cadastrado com sucesso!")
            st.rerun()

st.divider()

st.subheader("Ações de Sorteio")

col1, col2 = st.columns(2)

with col1:
    if st.button("Sortear 1 Aluno", key="btn_um", use_container_width=True):
        if not alunos:
            st.error("A lista de alunos está vazia!")
        else:
            st.session_state.tipo_sorteio = "unico"
            st.session_state.resultado_sorteio = random.choice(alunos)

    if st.session_state.tipo_sorteio == "unico" and st.session_state.resultado_sorteio:
        st.success(f"Aluno(a) sorteado(a): **{st.session_state.resultado_sorteio}**")

with col2:
    max_qtd = max(1, len(alunos))
    qtd = st.number_input("Quantidade de alunos a sortear:", min_value=1, max_value=max_qtd, value=min(2, max_qtd), step=1)

    if st.button("Sortear Vários", key="btn_varios", use_container_width=True):
        if len(alunos) < qtd:
            st.error("A quantidade solicitada é maior que o total de alunos cadastrados!")
        else:
            st.session_state.tipo_sorteio = "varios"
            st.session_state.resultado_sorteio = random.sample(alunos, k=qtd)

    if st.session_state.tipo_sorteio == "varios" and st.session_state.resultado_sorteio:
        st.success("Alunos sorteados:")
        for idx, a in enumerate(st.session_state.resultado_sorteio, start=1):
            st.markdown(f"**{idx}.** {a}")

with st.sidebar:
    st.header("Gerenciamento")
    st.metric("Total de Alunos", len(alunos))

    st.divider()
    aluno_remover = st.selectbox("Remover aluno:", [""] + alunos)
    if st.button("Remover", use_container_width=True):
        if aluno_remover:
            alunos.remove(aluno_remover)
            salvar_alunos(alunos)
            st.success(f"'{aluno_remover}' removido!")
            st.rerun()

    st.divider()
    if st.button("Restaurar Alunos Padrão", use_container_width=True):
        salvar_alunos(ALUNOS_PADRAO)
        st.session_state.resultado_sorteio = None
        st.session_state.tipo_sorteio = None
        st.success("Lista restaurada!")
        st.rerun()
