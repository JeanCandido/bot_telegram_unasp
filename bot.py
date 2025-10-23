import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")
updates = requests.get(f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/getUpdates")
updates = updates.json()
print(updates['result'][1])

#leu my friendo
