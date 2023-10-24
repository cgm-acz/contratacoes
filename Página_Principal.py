import streamlit as st
import json
import os

st.set_page_config(
    page_title="Página Principal",
    page_icon="📈",
)

st.image('logo.jpeg', caption=None, width=595, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.markdown("# Página Principal")

st.write(
    """Este programa foi desenvolvido com a exclusiva finalidade de testes e visa facilitar a análise de processos de licitações e contratos no âmbito da administração pública."""
)
st.write("\n")

st.subheader("Cadastro de Clientes")
cic_new = st.selectbox("Informe a função que deseja utiliza:" ["Análise de Licitações", "Análise de Contratos"])
