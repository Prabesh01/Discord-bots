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
    print(str(message.author)+' | '+str(guild)+' ('+str(channel)+')')
    embeds = message.embeds
    for embed in embeds:
        print(embed.to_dict())
    try:
        attachment_url = message.attachments[0].url
        print('Attatchment!!!!!!!!!!!: \n'+str(attachment_url))    
        # file_request = requests.get(attachment_url)
        # print(file_request.content)    
    except:
        pass
    print('Message:'+str(message.content)+"\n")
    
c.run(DISCORD_TOKEN)
