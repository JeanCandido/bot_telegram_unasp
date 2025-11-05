import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")

s = requests.Session()
res = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)

linha = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Linha/Buscar?termosBusca=Interlagos"
)
linha = linha.json()
print(linha[0])

# res = s.get(
#     f"http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha={cl}"
# )
# paradas = res.json()

# pos = s.get(
#     "http://api.olhovivo.sptrans.com.br/v2.1//Posicao/Linha?codigoLinha=2506"
# )
# print(pos.json()['vs'][0]['py'], pos.json()['vs'][0]['px'])