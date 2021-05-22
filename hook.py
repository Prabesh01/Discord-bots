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
        time=str(post['post_id'])
        f = open("r.txt", "r")
        prev=f.read()
        old=re.search(time, prev)
        if old==None: 
            if(str(post['video'])!='None'):
              webhook = DiscordWebhook(username='Routiney', avatar_url='https://pbs.twimg.com/profile_images/777188003445739521/t5GNGfAc_400x400.jpg', url=hooks, content=str(post['text'])+'\n<'+str(post['post_url'])+'>\n'+str(post['video']))
              webhook.execute()
              continue
            webhook = DiscordWebhook(username='Routiney', avatar_url='https://pbs.twimg.com/profile_images/777188003445739521/t5GNGfAc_400x400.jpg', url=hooks)
            embed = DiscordEmbed(description=str(post['text']))            
            embed.set_author(name='Routiney', url=post['post_url'], icon_url='https://pbs.twimg.com/profile_images/777188003445739521/t5GNGfAc_400x400.jpg')
            img = post['images']
            try:
                imgcount=len(img)
                if(imgcount>2):
                    webhook.add_embed(embed)
                    webhook.execute()
                    for imgs in post['images']:
                        webhook = DiscordWebhook(username='Routiney', avatar_url='https://cdn.discordapp.com/app-icons/786534057437691914/8dd876fd77d51452a5e3b3df4bc0ce18.png?size=256', url=hooks)
                        embed = DiscordEmbed(description='\u200b')
                        embed.set_image(url=imgs)
                        webhook.add_embed(embed)
                        webhook.execute()
                else:
                    try:
                        embed.set_image(url=img[1])
                        embed.set_thumbnail(url=img[0])
                    except:
                        embed.set_image(url=post['image'])
                    embed.set_footer(text='Blah Blah Blah ...') 
                    webhook.add_embed(embed)
                    response = webhook.execute()
             except:
                    embed.set_image(url=post['image'])
                    webhook.add_embed(embed)
                    webhook.execute()                    
            last=str(post['time'])
            f = open("r.txt", "a")
            f.write(last)
            f.close()
    ok()

                 
def ok():
    print('WORKEDDDD !!!!!!')
           
routiney()
