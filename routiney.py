import discord
import re
import os
import sys
from os import path
from dotenv import load_dotenv
import requests
import random
from facebook_scraper import get_posts


c = discord.Client()

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

def fl(name):
    if path.exists(name) !=True:
        f = open(name, "a")
        f.close()

@c.event
async def on_ready():
    fl('list.txt')
    f=open('list.txt','r')
    f=f.read()
    f=f.split()
    total=len(f)
    if total==0:
        return
    for i in range(0, total):
        chd=int(f[i])
        channel = c.get_channel(chd)
        if channel==None:
            continue
        for post in get_posts('officialroutineofnepalbanda', pages=1):
            fl('r.txt')
            time=str(post['time'])
            f = open("r.txt", "r")
            prev=f.read()
            old=re.search(time, prev)
            if old==None: 
                if post['image']==None:
                    channel = c.get_channel(chd)
                    await channel.send(str(post['text']))
                elif post['text']==None:
                    channel = c.get_channel(chd)
                    e = discord.Embed()
                    e.set_image(url=post['image'])
                    await channel.send(embed=e)
                else:
                    channel = c.get_channel(chd)
                    await channel.send(str(post['text']))
                    e = discord.Embed()
                    e.set_image(url=str(post['image']))
                    await channel.send(embed=e)
                last=str(post['time'])
                f = open("r.txt", "a")
                f.write(last)
                f.close()                



@c.event
async def on_message(message):
    if message.author == c.user:
        return    
    
    who = [
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
        response = random.choice(who)
        await message.channel.send(response)
        
    if message.content == 'r!sub':
        clts = str(message.channel.id)
        if path.exists('list.txt') !=True:
            f = open('list.txt', "a")
            f.close()
        f = open("list.txt", "r")
        prev=f.read()
        old=re.search(clts, prev)
        if old==None: 
            f = open("list.txt", "a")
            f.write(clts+'\n')
            f.close()
            await message.channel.send("This channel is subscribed to receive routiney's new shits\nUse r!unsub to unsubscribe")
        if old!=None:
            await message.channel.send("This channel was already subscribed") 
            
            
    if message.content == 'r!unsub':
        clts = str(message.channel.id)
        if path.exists('list.txt') !=True:
            f = open('list.txt', "a")
            f.close()
        f = open("list.txt", "r")
        prev=f.read()
        old=re.search(clts, prev)
        if old!=None: 
            fin = open("list.txt", "rt")
            data = fin.read()
            data = data.replace(clts, '')
            fin.close()
            fin = open("list.txt", "wt")
            fin.write(data)
            fin.close()
            await message.channel.send("This channel is unsubscribed sucessflly")
        if old==None:
            await message.channel.send("This channel was never subscribed\nUse r!sub to sunscribe")                
           
           
c.run(DISCORD_TOKEN)
