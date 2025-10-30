import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")

def updates():
  updates = requests.get(f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/getUpdates?offset=-1")
  updates = updates.json()
  last_update = updates["result"][0]
  if last_update:
    last_date = last_update["message"]["date"]
  return last_update["message"]["chat"]["id"], last_update["message"]["text"], last_date



upd = updates()

id = upd[0]

x = eval(upd[1])



print(x)

# while True:
#   try:
#     upd = updates()
#     if upd[2] > last_date:
#       id = upd[0]
#       text = eval(upd[1])
#       last_date = upd[2]
#       requests.post(
#         url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendLocation",
#         data= {"chat_id": id, "latitude": -23.589616, "longitude": -46.682964}
#         ).json()
#     else:
#       requests.post(
#         url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage",
#         data= {"chat_id": id, "text": "Operação Impossivel"}
#       ).json()
#   except:
#     pass

import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")

s = requests.Session()
res = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)

linhas_lapa = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Linha/Buscar?termosBusca=Penha"
)
linhas_lapa = linhas_lapa.json()
cl = linhas_lapa[0]['cl']

res = s.get(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha={cl}"
)
paradas = res.json()

pos = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1//Posicao/Linha?codigoLinha=175"
)
x1 = pos.json()['vs'][0]['py']
x2 = pos.json()['vs'][0]['px']

requests.post(
    url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendLocation",
    data= {"chat_id": id, "latitude": x1, "longitude": x2}
    )