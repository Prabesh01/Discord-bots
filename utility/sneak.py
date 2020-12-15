import discord
import os
from dotenv import load_dotenv

c = discord.Client()

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

@c.event
async def on_ready():
    pass     

@c.event
async def on_message(message):
    if message.author == c.user:
        return  
    print('Sender: '+str(message.author))
    clts = message.channel.id
    channel = c.get_channel(clts)
    print('Channel: ',channel)
    ID = message.guild.id
    guild = c.get_guild(ID)
    print('Server: '+str(guild))    
    print('Message:'+str(message.content)+"\n")
    
c.run(DISCORD_TOKEN)
