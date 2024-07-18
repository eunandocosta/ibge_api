import requests

# URL da API do IBGE para obter os municípios
url_municipios = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
response = requests.get(url_municipios)
data_municipios = response.json()

# Dicionário para armazenar os estados com seus respectivos índices e municípios
estados_e_municipios = {}
indice = 1

# ID do indicador de renda média (Exemplo: 30255 é um indicador fictício)
indicador_renda_media = "44"  # ID da PNAD para renda média

# Itera sobre os dados retornados dos municípios
for item in data_municipios:
    nome_municipio = item["nome"]
    nome_estado = item["microrregiao"]["mesorregiao"]["UF"]["nome"]
    sigla_estado = item["microrregiao"]["mesorregiao"]["UF"]["sigla"]
    id_municipio = item["id"]

    # URL para obter a renda média do município
    url_renda_media = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/indicadores/{indicador_renda_media}/resultados/{id_municipio}"
    
    response_renda_media = requests.get(url_renda_media)
    if response_renda_media.status_code == 200:
        try:
            data_renda_media = response_renda_media.json()
            # Supondo que a estrutura da resposta contém um campo 'res' com o valor
            if data_renda_media:
                renda_media = data_renda_media[0].get("res", "N/A")
            else:
                renda_media = "N/A"
        except ValueError:
            renda_media = "N/A"
    else:
        renda_media = "N/A"

    # Se o estado já está no dicionário, adiciona o município à lista
    if nome_estado in estados_e_municipios:
        estados_e_municipios[nome_estado]["municipios"].append({
            "nome": nome_municipio,
            "renda_media": renda_media
        })
    # Se o estado não está no dicionário, cria uma nova entrada
    else:
        estados_e_municipios[nome_estado] = {
            "indice": indice,
            "sigla": sigla_estado,
            "municipios": [{
                "nome": nome_municipio,
                "renda_media": renda_media
            }]
        }
        indice += 1

# Exibe os estados com seus índices, siglas e respectivos municípios com renda média
for estado, info in estados_e_municipios.items():
    print(f"Estado: {estado} (Sigla: {info['sigla']})")
    for municipio in info["municipios"]:
        print(f"  - {municipio['nome']} (Renda Média: {municipio['renda_media']})")
