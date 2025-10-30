import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")

s = requests.Session()
res = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)

def updates():
  updates = requests.get(f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/getUpdates?offset=-1")
  updates = updates.json()
  last_update = updates["result"][0]
  if last_update:
    last_date = last_update["message"]["date"]
  return last_update["message"]["chat"]["id"], last_update["message"]["text"], last_date

last_date = 0

while True:
  try:
    upd = updates()
    contador = 0
    if upd[2] > last_date:
      id = upd[0]
      text = upd[1]
      last_date = upd[2]
      linha = s.get(
          f"http://api.olhovivo.sptrans.com.br/v2.1/Linha/Buscar?termosBusca={text}"
      ).json()
      cl = s.get(
          f"http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha={linha[contador]['cl']}"
      ).json()
      if cl == []:
        contador += 1
      print(cl)
      py = cl[0]['py']
      px = cl[0]['px']
      
      print(px)
      print(py)
      

      requests.post(
        url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendLocation",
        data= {"chat_id": id, "longitude": px, "latitude": py}
      ).json()
  except:
    pass