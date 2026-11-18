import streamlit as st

st.set_page_config(page_title="Prova Bimestral - Prática", layout="wide")

if "calculado" not in st.session_state:
    st.session_state.calculado = False
    st.session_state.resultado = 0

with st.container(horizontal_alignment='left', vertical_alignment='top'):
    left, dire = st.columns([9, 1])
    
    with left:
        st.title("IMC Inteligente")
        st.text("Sua saúde começa com informação.")

with st.container(horizontal_alignment='left', vertical_alignment='top'):
    left, dire = st.columns([9, 1])
    
    with left:
        st.title("Calcule seu IMC")
        st.text("Preencha os campos abaixo para calcular seu índice de massa corporal.")

    in_left, in_dir = st.columns(2)
    with in_left:
        peso_input = st.text_input("**Peso (Kg)**", key="peso_input")
    with in_dir:
        altura_input = st.text_input("**Altura (m)**", key="altura_input")
    
    if(st.button("Calcular meu IMC", use_container_width=True, type='primary')):
        st.session_state.resultado = 0
        if(not peso_input.strip() or not altura_input.strip()):
            st.warning("As duas medidas são necessárias para calcular o IMC.")
            st.rerun()
        else: 
            try:
                peso = float(peso_input.replace(',', '.'))
                altura = float(altura_input.replace(',', '.'))
                if(peso < 0 or altura < 0):
                    st.error("Ambos os valores precisam ser maiores que 0.")
                else:
                    st.session_state.resultado = peso / (altura * altura)
            except Exception:
                st.error("As duas medidas precisam ser números decimais.")

st.divider()

st.markdown("SEU RESULTADO")

st.write(f"{st.session_state.resultado:.2f}")
if(st.session_state.resultado > 0):
    if(st.session_state.resultado < 18.5):
        st.error("Abaixo do peso - Peso abaixo da faixa de referência para adultos")
    elif(st.session_state.resultado < 25):
        st.success("Peso normal - Peso dentro da faixa de referência para adultos")
    elif(st.session_state.resultado < 30    ):
        st.warning("Acima do peso - Peso acima da faixa de referência para adultos")
    else:
        st.error("Obesidade - Peso muito acima da faixa de referência para adultos")


st.text("O IMC é um indicador geral e não substitui uma avaliação profissional de saúde.")