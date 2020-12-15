from discord import Webhook, RequestsWebhookAdapter
import discord
import os
from dotenv import load_dotenv

c = discord.Client()

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

@c.event
async def on_ready():
    f = open('hook.txt')
    for line in f: 
        webhook = Webhook.from_url(line, adapter=RequestsWebhookAdapter())
        webhook.send("Hello World")

c.run(DISCORD_TOKEN)
