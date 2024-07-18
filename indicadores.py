import requests

url_pesquisas = "https://servicodados.ibge.gov.br/api/v1/pesquisas"
response_pesquisas = requests.get(url_pesquisas)
data_pesquisas = response_pesquisas.json()

list_pesquisas = {}

for item in data_pesquisas:
    list_pesquisas[item["id"]] = item["nome"]

indicadores = "https://servicodados.ibge.gov.br/api/v1/pesquisas/44/indicadores"
response_indicadores = requests.get(indicadores)
data_indicadores = response_indicadores.json()

list_indicadores = {}

for item in data_indicadores:
    list_indicadores[item["id"]] = item["indicador"]


indicadores = "https://servicodados.ibge.gov.br/api/v1/pesquisas/44/indicadores/47044"
response_indicadores = requests.get(indicadores)
data_indicadores = response_indicadores.json()

list_indicadores = {}

for item in data_indicadores:
    print(item["children"])
