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
    'latiko poi',
    'khate bahun'
    ]
    if message.content == "r!":
        member=message.guild.me
        perm_list = [perm[0] for perm in message.channel.permissions_for(member) if perm[1]]
        if not('manage_webhooks' in perm_list):
          await message.channel.send("Grrrr. I don't have permission to manage webhooks. You must provide me that permission in order to use me.\nFacing any issue with the bot? Inform me: Prabesh#1134")
          return
        if not('embed_links' in perm_list):
          await message.channel.send("Grrrr. I don't have permission to embed links. I would need that permission to show you images and videos.\nAny  issues with the bot? Inform me: Prabesh#1134")
          return 
        if not('read_message_history' in perm_list):
          await message.channel.send("I don't have permission to read message history. This permisson isn't compulsory but you won't be able to use // command to delete messages of the channel\nFor more information, contact: Prabesh#1134")
          return
        if('administrator' in perm_list):
          await message.channel.send("Everything is just perfect!\nFeel free to contact me if you faced any issue: Prabesh#1134")
          return        
        await message.channel.send("Looks like you set me up well\nFeel free to contact me if you faced any issue: Prabesh#1134")

    if message.content == 'oa':
        response = random.choice(oa)
        await message.channel.send(response)
          
    if message.content == 'r!sub':
        if message.author.guild_permissions.administrator:
            pass
        else:
            await message.channel.send("Only server admins are allowed to use this command!")
            return
        member=message.guild.me
        perm_list = [perm[0] for perm in message.channel.permissions_for(member) if perm[1]]
        if not('manage_webhooks' in perm_list):
          await message.channel.send("Grrrr. I don't have permission to manage webhooks. You must provide me that permission in order to use me.")
          return    
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
            await message.channel.send("This channel is subscribed to receive routiney's new shit\nUse r!unsub to unsubscribe\nFeel free to contact me if you faced any issue: Prabesh#1134")
        if old!=None:
            await message.channel.send("This channel was already subscribed. \n Use r!unsub to unsubscribe first.") 
                        
    if message.content == 'r!unsub':
        if message.author.guild_permissions.administrator:
            pass
        else:
            await message.channel.send("Only server admins are allowed to use this command!")
            return       
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
            await message.channel.send("This channel is unsubscribed sucessfully\nFeel free to send me your feedbacks/complaints: Prabesh#1134")
        if old==None:
            await message.channel.send("This channel was never subscribed\nUse r!sub to sunscribe\nUse r!sub to subscribe")                     
c.run(DISCORD_TOKEN)
