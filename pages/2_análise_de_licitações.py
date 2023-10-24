import requests
import pandas as pd

url = "http://wstransparencia.pma.es.gov.br/api/programas/anos"


response = requests.get(url)
st.write(response.json())
