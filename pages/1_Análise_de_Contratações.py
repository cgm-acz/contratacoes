import streamlit as st
import datetime as d
from datetime import date
import pandas as pd

tipos = ['Análise de risco', 'Seleção de processos']

st.image('logo.jpeg', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.sidebar.markdown("# Página Principal")

st.title('Sistema de Análise de Contratações:')

licitacao = st.selectbox(
    'Selecione o tipo de processo de contratação:',
    ('Dispensa', 'Inexigibilidade', 'Concorrência'))
st.write('Selecionado:', licitacao)

data = st.date_input(
    "Selecione a data inicial dos registros:",
    d.date(2000, 1, 1))
st.write('Verificando registros de', data)

date_select = st.sidebar.radio("Selecione a aplicação:", tipos)

risco = st.slider('Selecione o fator de risco a ser utilizado:', 0, 100, 50)
st.write("O fator de risco definido foi", risco)

ativos = st.number_input('Digite o valor dos ativos:', value=1)
passivos = st.number_input('Digite o valor dos passivos:', value=1)
geral = ativos / passivos
if geral >= 1:
 st.write('A liquidez geral da empresa é', geral, '- Índice suficiente e adequado.')
elif geral < 1:
 st.write('A liquidez geral da empresa é', geral, '- índice insuficiente e inadequado.')
ativo_circulante = st.number_input('Digite o valor do ativo circulante:', value=1)
passivo_circulante = st.number_input('Digite o valor do passivo circulante:', value=1)
corrente = ativo_circulante / passivo_circulante
if corrente >= 1:
 st.write('A liquidez corrente da empresa é', corrente, '- Índice suficiente e adequado.')
elif corrente < 1:
 st.write('A liquidez corrente da empresa é', corrente, '- índice insuficiente e inadequado.')

if st.button('Gerar teste de conformidade.'):
    st.write('Teste de conformidade gerado com sucesso.')

from datetime import date

url="https://docs.google.com/spreadsheets/d/e/2PACX-1vRONBMGF9sCcIHjWp3UlD-x1np1CCgXoMl4pdMhidfkPpA3K6GUiTKe35sW3-QA8-_D_xo64nYBzGYV/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)
st.dataframe(df)

def idade(nascimento):
  today = date.today()
  idade = today.year - nascimento.year - ((today.month, today.day) < (nascimento.month, nascimento.day))
  return idade
  resultado = ((idade)(date(1960, 10, 1)))
  if resultado >= 60:
   print("O servidor possui", resultado, "anos.", "Portanto, o servidor atingiu a idade mínima.")
  elif resultado < 60:
   print("O servidor possui", resultado, "anos.", "Portanto, o servidor não atingiu a idade mínima.")
