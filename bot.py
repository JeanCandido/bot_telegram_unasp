import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")
updates = requests.get(f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/getUpdates")
updates = updates.json()
<<<<<<< HEAD
print(updates["result"][-1])
=======
print(updates['result'][1])
>>>>>>> b72989143db8d9f970e712fafd0f9df1c9e75e58

#leu my friendo
