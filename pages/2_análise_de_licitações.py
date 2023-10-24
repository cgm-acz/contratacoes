import requests
import pandas as pd

lic = st.input_text("Informe o número da licitação:")

if lic:  
  url = "http://wstransparencia.pma.es.gov.br/api/Licitacao/" + lic
  
  response = requests.get(url)
  
  data = response.json()
  
  df = pd.DataFrame(data)
  st.write(df)
