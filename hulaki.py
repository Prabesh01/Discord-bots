import requests
import re
import sys
import os.path
from os import path
from discord_webhook import DiscordWebhook, DiscordEmbed

wurl="Webhook_URL_Here"
xs="XS_VALUE_HERE"
useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
cid="C_USER VALUE HERE"

def fl(name):
    if path.exists(name) !=True:
        f = open(name, "a")
        f.close()


cookies = {
    'xs': xs,
    'c_user': cid,
}

headers = {
    'User-Agent': useragent,
}

response = requests.get('https://m.facebook.com/messages/', headers=headers, cookies=cookies)
out=response.text

try:
    scrap=re.findall('<!--.*?-->', out, re.DOTALL)
    scrapp=re.findall('_52jd _52.*?<span', scrap[0], re.DOTALL)
    scrapp=re.sub('_52jd _52.*?">', '', scrapp[0])
    user=re.sub('<span', '', scrapp)
    user=re.sub('</h3>', '', user)

    scrappe=re.findall('snippet ellipsis _3z10 _3z11.*?</span>', scrap[0], re.DOTALL)
    scrappe=re.sub('snippet ellipsis _3z10 _3z11">', '', str(scrappe[0]))
    message=re.sub('</span>', '', str(scrappe))
    if re.search('class="', message):
        message='seems like mesaage contains an attatchment or an emoji'
except:
    user="Hulaki Error Reporting"
    message="Something went wrong. Most probably, the provided values might have expired."

fl('fb.txt')
f = open("fb.txt", "r")
prev=f.read()
old=re.search(re.escape(user), str(prev).strip())
oldm=re.search(re.escape(message), str(prev).strip())
if any( [old == None, oldm == None] ):
    webhook = DiscordWebhook(username='Hulaki', avatar_url='https://i.pinimg.com/564x/98/1a/ea/981aea34c2ce10a6b39e3192a518b88e.jpg', url=wurl, content="New Conversation with "+user+": "+message)
    response = webhook.execute()
    f = open("fb.txt", "w")
    f.write(str(user)+"\n"+str(message))
    f.close()
