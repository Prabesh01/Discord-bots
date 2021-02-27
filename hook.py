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
            embed.set_author(name='Routiney', url=post['post_url'], icon_url='https://pbs.twimg.com/profile_images/777188003445739521/t5GNGfAc_400x400.jpg')
            img = post['images']
            try:
                embed.set_image(url=img[1])
                embed.set_thumbnail(url=img[0])
            except:
                embed.set_image(url=post['image'])
            embed.set_footer(text='Blah Blah Blah ...') 
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
