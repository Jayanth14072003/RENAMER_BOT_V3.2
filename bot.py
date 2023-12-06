import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6100891233:AAHo_OjnFWTdY_JewRdcqphxASAcAK1IHVg")

API_ID = int(os.environ.get("API_ID", "3393749"))

API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

STRING = os.environ.get("STRING", "BQDMOvAACtNs-VchfumyK9k5-nCNC07ktlBNprSCibT8v6TlKUld6ZCdmSweiwaB9dYKGUGUDJoVmwk76Di47l9KaeEfBO_6ly7autQqKVoaV0t51FOqxtQQ5sm1zKT4qfvV0zUnw-2nY4yUEzCJJ-2OADSkzQXUDWq_0R1WEDvDOrwUVu6Q92Yliu3yOvUe-yYF9Cd9aiUZO8oOl2Lr5ljVBOQXD1s-acZV_80Ltf20fTkuYym6Bv1zrdvyXuyiBBaQKv_cwHaXcjmAlxvmQaBE-N75q8C_TazXigo0Uflhpqj7MzZoLJZQWw15Tci7RITeErIKtRFC7u6JhnbLDIEZ_uuWYgAAAABZsWSfAA")


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
