import requests
import re
import os.path
from os import path
from dotenv import load_dotenv
from facebook_scraper import get_posts
from discord_webhook import DiscordWebhook, DiscordEmbed



def fl(name):
    if path.exists(name) !=True:
        f = open(name, "a")
        f.close()
        
def routiney():
    fl('r.txt')
    fl('hook.txt')
    f=open('hook.txt','r')
    f=f.read()
    hooks=f.split()
    total=len(f)
    if total==0:
        return
    for post in get_posts('officialroutineofnepalbanda', pages=1):
        time=str(post['time'])
        f = open("r.txt", "r")
        prev=f.read()
        old=re.search(time, prev)
        if old==None: 
            webhook = DiscordWebhook(username='Routiney', avatar_url='https://pbs.twimg.com/profile_images/777188003445739521/t5GNGfAc_400x400.jpg', url=hooks)
            embed = DiscordEmbed(description=str(post['text']))
            embed.set_image(url=post['image'])
            webhook.add_embed(embed)
            response = webhook.execute()
            print(response)
            last=str(post['time'])
            f = open("r.txt", "a")
            f.write(last)
            f.close()
    ok()

                 
def ok():
    print('WORKEDDDD !!!!!!')
           
routiney()
