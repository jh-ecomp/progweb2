import random
import streamlit as st

st.markdown("""
    <style>
        div[data-testid="stMarkdownContainer"] p, p {
            font-size: 30px !important;
        }

        [data-testid="stWidgetLabel"] p,
        [data-testid="stWidgetLabel"] label {
            font-size: 24px !important;
        }

        .stNumberInput input {
            font-size: 24px !important;
            height: auto !important;
        }
    </style>
""", unsafe_allow_html=True)



if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 100)
    st.session_state.tentativas = 0
    st.session_state.palpites = []
    st.session_state.done = False

st.title("🎮 DESAFIO DO NÚMERO SECRETO")
st.markdown("<p>Descubra o número secreto entre 1 e 100.</p>", unsafe_allow_html=True)

palpite = st.number_input("Informe seu palpite:", min_value=1, max_value=100, step=1)

coluna_tentativas, coluna_palpites = st.columns([1, 2])


if st.button("Palpitar", disabled=st.session_state.done, use_container_width=True):
    st.session_state.tentativas += 1
    st.session_state.palpites.append(palpite)
    if palpite < st.session_state.numero_secreto:
        st.warning("Tente um número maior!")
    elif palpite > st.session_state.numero_secreto:
        st.error("Tente um número menor!")
    else:
        st.session_state.done = True
        st.success(f"Parabéns! Você acertou em {st.session_state.tentativas} tentativas!")


with coluna_tentativas:
    st.write(f"Tentativas: {st.session_state.tentativas}")

with coluna_palpites:
    if st.session_state.palpites:
        palpites_formatados = ", ".join(map(str, st.session_state.palpites))
        st.markdown(f"**Palpites:** {palpites_formatados}")



with st.sidebar:
    if st.button("Novo Jogo"):
        st.session_state.numero_secreto = random.randint(1, 100)
        st.session_state.tentativas = 0
        st.session_state.palpites = []
        st.session_state.done = False
        st.rerun()