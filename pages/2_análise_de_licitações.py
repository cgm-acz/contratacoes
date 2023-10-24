import requests
import json

url = "http://wstransparencia.pma.es.gov.br/api/programas/anos"

# Faz uma solicitação GET para a URL
response = requests.get(url, timeout=15)

# Verifica se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Analisa o conteúdo JSON da resposta
    data = json.loads(response.text)

    # Exibe as informações
    for item in data:
        print(f"Nome: {item['Nome']}")
        print(f"Valor: {item['Valor']}")
        print()
else:
    print(f"A solicitação falhou com o código de status {response.status_code}")
