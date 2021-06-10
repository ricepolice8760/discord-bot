# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('ODQyMDQ0NTg3MjA4MDgxNDI4.YJvlIg.DIxPOfB-7oOEEPUAa8YUcpok5Mw')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)