import requests
import streamlit as st

st.set_page_config(page_title="Jogo de Cartas", layout="centered")

VALORES_CARTAS = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "JACK": 11,
    "QUEEN": 12,
    "KING": 13,
    "ACE": 14,
}

NAIPES_PT = {
    "SPADES": "Espadas ♠",
    "HEARTS": "Copas ♥",
    "DIAMONDS": "Ouros ♦",
    "CLUBS": "Paus ♣",
}

VALORES_PT = {
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "10",
    "JACK": "Valete",
    "QUEEN": "Dama",
    "KING": "Rei",
    "ACE": "Ás",
}

if "vitorias_j1" not in st.session_state:
    st.session_state.vitorias_j1 = 0
    st.session_state.vitorias_j2 = 0
    st.session_state.empates = 0
    st.session_state.carta_j1 = None
    st.session_state.carta_j2 = None
    st.session_state.resultado = None

st.title("🃏 Batalha de Cartas")
st.markdown("Cada jogador recebe uma carta sorteada da API e a de maior valor vence a rodada!")
st.divider()

if st.session_state.carta_j1 and st.session_state.carta_j2:
    col_j1, col_j2 = st.columns(2)

    with col_j1:
        c1 = st.session_state.carta_j1
        st.subheader("Jogador 1")
        st.image(c1["image"], width=180)
        nome_valor = VALORES_PT.get(c1["value"], c1["value"])
        nome_naipe = NAIPES_PT.get(c1["suit"], c1["suit"])
        st.markdown(f"**Carta:** {nome_valor} de {nome_naipe}")
        st.markdown(f"**Valor numérico:** {VALORES_CARTAS.get(c1['value'], 0)}")

    with col_j2:
        c2 = st.session_state.carta_j2
        st.subheader("Jogador 2")
        st.image(c2["image"], width=180)
        nome_valor = VALORES_PT.get(c2["value"], c2["value"])
        nome_naipe = NAIPES_PT.get(c2["suit"], c2["suit"])
        st.markdown(f"**Carta:** {nome_valor} de {nome_naipe}")
        st.markdown(f"**Valor numérico:** {VALORES_CARTAS.get(c2['value'], 0)}")

st.divider()

if st.button("Jogar", use_container_width=True):
    try:
        resposta = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=2")
        dados = resposta.json()

        if dados.get("success") and len(dados.get("cards", [])) >= 2:
            c1 = dados["cards"][0]
            c2 = dados["cards"][1]

            st.session_state.carta_j1 = c1
            st.session_state.carta_j2 = c2

            val1 = VALORES_CARTAS.get(c1["value"], 0)
            val2 = VALORES_CARTAS.get(c2["value"], 0)

            if val1 > val2:
                st.session_state.vitorias_j1 += 1
                st.session_state.resultado = ("j1", "🏆 Jogador 1 venceu a rodada!")
            elif val2 > val1:
                st.session_state.vitorias_j2 += 1
                st.session_state.resultado = ("j2", "🏆 Jogador 2 venceu a rodada!")
            else:
                st.session_state.empates += 1
                st.session_state.resultado = ("empate", "🤝 Empate!")
            st.rerun()
        else:
            st.error("Erro ao obter cartas da API.")
    except Exception as e:
        st.error(f"Não foi possível conectar à API de cartas: {e}")

st.divider()

col_p1, col_emp, col_p2 = st.columns(3)
with col_p1:
    st.metric("Vitórias Jogador 1", st.session_state.vitorias_j1)
with col_emp:
    st.metric("Empates", st.session_state.empates)
with col_p2:
    st.metric("Vitórias Jogador 2", st.session_state.vitorias_j2)


if st.session_state.resultado:
    tipo, msg = st.session_state.resultado
    if tipo == "empate":
        st.info(msg)
    else:
        st.success(msg)

with st.sidebar:
    st.header("Opções")
    if st.button("Novo Jogo / Zerar Placar", use_container_width=True):
        st.session_state.vitorias_j1 = 0
        st.session_state.vitorias_j2 = 0
        st.session_state.empates = 0
        st.session_state.carta_j1 = None
        st.session_state.carta_j2 = None
        st.session_state.resultado = None
        st.rerun()

    st.divider()
    st.markdown("### Regras")
    st.markdown(
        "- **Ás (A):** 14 pontos (maior carta)\n"
        "- **Rei (K):** 13 pontos\n"
        "- **Dama (Q):** 12 pontos\n"
        "- **Valete (J):** 11 pontos\n"
        "- **2 a 10:** valor da própria carta"
    )
