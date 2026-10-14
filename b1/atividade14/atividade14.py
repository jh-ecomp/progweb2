import streamlit as st

st.set_page_config(page_title="Portal Parnaíba Descontraída", layout="wide")

st.title("Portal Parnaíba Descontraída")
st.divider()

with st.container(horizontal_alignment='center', vertical_alignment='top'):
    esq, cent, dir = st.columns([0.2, 0.6, 0.2])
    
    with cent:
        st.title("Bem vindos à Parnaíba!")

        st.image('imagem-principal.jpg', caption="Porto das Barcas no entardecer. Foto de autor desconhecido.",
            alt="Porto das Barcas. Autor: Desconhecido. Técnica: Fotografia")
        
        st.markdown(
            """
            <p style="text-align: justify;">
                Capital do Delta e coração do litoral piauiense, Parnaíba combina a leveza dos ventos costeiros com a energia pulsante de um povo acolhedor e cheio de histórias para contar. Entre o charme dos casarões coloniais do Porto das Barcas, a riqueza da gastronomia típica e a imponência do encontro dos rios com o mar, a cidade respira natureza exuberante, cultura vibrante e um estilo de vida descontraído que conquista qualquer visitante à primeira vista.
            </p>
            <p style="text-align: justify;">
                Prepare as malas, respire fundo essa brisa e venha descobrir com a gente os melhores destinos turísticos e as experiências inesquecíveis que só Parnaíba e seus arredores têm a oferecer!
            </p>
            """,
            unsafe_allow_html=True,
        )


with st.sidebar:
    st.image("logo.jpeg", width=100)
    st.header("Navegação")
    st.markdown("📍 Destinos")
    st.markdown("📷 Galeria")
    st.markdown("📁 Materiais")
    st.markdown("🔗 Links")
    st.markdown("📞 Contato")
    st.markdown("⭐ Avaliação")