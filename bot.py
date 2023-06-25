import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "1865366440:AAEa-2W3GbTQ8pdm7-uGbLZOtKRVUB2cHIY")

API_ID = int(os.environ.get("API_ID", "3393749"))

API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
