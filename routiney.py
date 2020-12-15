import discord
import re
import os
from os import path
from dotenv import load_dotenv
import requests
import random
from discord_webhook import DiscordWebhook

c = discord.Client()

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

def fl(name):
    if path.exists(name) !=True:
        f = open(name, "a")
        f.close()

@c.event
async def on_ready():
    await c.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to r! , r!sub, r!unsub"))
    pass              

@c.event
async def on_message(message):
    if message.author == c.user:
        return    
    
    oa = [
    'Chup mug',
    'disturb vo mug',
    'jurukka uthera jhyamma mukh padkau!',
    'Sutna dyao, chuppa lara!',
    'Turi tandim tero?',
    'khate bahun'
    ]
    if message.content == "r!":
        await message.channel.send("Looks like you set me up well\nUse r!sub to start getting new posts by RONB\nContact Prabesh#1134 if you want to receive updates from other pages as well")

    if message.content == 'oa':
        response = random.choice(oa)
        await message.channel.send(response)
          
    if message.content == 'r!sub':
        clts = message.channel.id
        channel = c.get_channel(clts)  
        clts=str(clts)    
        fl('list.txt')
        f = open("list.txt", "r")
        prev=f.read()
        old=re.search(clts, prev)
        if old==None: 
            f = open("list.txt", "a")
            f.write(clts+'\n')
            f.close()
            web=await channel.create_webhook(name='Routiney')
            clts=web.url
            fl('hook.txt')
            f = open("hook.txt", "a")
            f.write(clts+'\n')
            f.close()               
            await message.channel.send("This channel is subscribed to receive routiney's new shits\nUse r!unsub to unsubscribe")
        if old!=None:
            await message.channel.send("This channel was already subscribed") 
                        
    if message.content == 'r!unsub':
        clts = message.channel.id
        clt=str(clts)
        fl('list.txt')
        f = open("list.txt", "r")
        prev=f.read()
        old=re.search(clt, prev)
        if old!=None: 
            fin = open("list.txt", "rt")
            data = fin.read()
            data = data.replace(clt, '')
            fin.close()
            fin = open("list.txt", "wt")
            fin.write(data)
            fin.close()
            for hook in await message.channel.webhooks(): 
                hoo=re.sub(r'\D','',str(hook))           
                fname = 'hook.txt'
                f = open(fname)
                output = []
                for line in f:
                    if not hoo in line:
                        output.append(line)
                    if hoo in line:
                        await hook.delete()                        
                f.close()
                f = open(fname, 'w')
                f.writelines(output)
                f.close()            
            await message.channel.send("This channel is unsubscribed sucessfully")
        if old==None:
            await message.channel.send("This channel was never subscribed\nUse r!sub to sunscribe")                     
c.run(DISCORD_TOKEN)
