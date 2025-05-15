from pathlib import Path
import streamlit as st
import helper
import settings

st.set_page_config(
    page_title="EcoClasificador Upsa",
)

st.sidebar.title("Consola de Detección de Residuos")

model_path = Path(settings.DETECTION_MODEL)

st.title("EcoClasificador Upsa: Sistema Inteligente de Clasificación de Residuos")
st.write("Clasificación de residuos en tiempo real usando IA")
st.markdown(
"""
<style>
    .stRecyclable {
        background-color: rgba(233,192,78,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        margin-top: 0 !important;
        font-size:18px !important;
    }
    .stNonRecyclable {
        background-color: rgba(94,128,173,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        margin-top: 0 !important;
        font-size:18px !important;
    }
    .stHazardous {
        background-color: rgba(194,84,85,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        margin-top: 0 !important;
        font-size:18px !important;
    }

</style>
""",
unsafe_allow_html=True
)

try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"No se puede abrir el modelo: {model_path}")
    st.error(ex)
helper.play_webcam(model)

st.sidebar.markdown("Créditos: Nicole Numberg, Teresa Cossio, Oscar Aguilar, Jorge Urioste, Jorge Saucedo", unsafe_allow_html=True)