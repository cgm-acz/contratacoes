import requests
import pandas as pd
import streamlit as st

lic = st.number_input("Informe o número da licitação:")

if lic:  
  url = "http://wstransparencia.pma.es.gov.br/api/Licitacao/" + lic
  
  response = requests.get(url)
  
  data = response.json()
  
  df = pd.DataFrame(data)
  st.write(df)
