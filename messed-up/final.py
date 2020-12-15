import requests
import re
from time import time, sleep

from facebook_scraper import get_posts

def routiney():
    for post in get_posts('officialroutineofnepalbanda', pages=1):
    # print('TIME: '+str(post['time'])+'\n')
    # print(post['text']+'\n')
    # print('Image: '+post['image']+'\n')
    # print('Link to Post: '+post['post_url']+'\n\n')
        time=str(post['time'])
        f = open("r.txt", "r")
        prev=f.read()
        old=re.search(time, prev)
        if old==None: 
        #if time!=prev:
            if str(post['image'])!='None':
                data = {
                'username': 'Routiney',
                'avatar_url': 'https://pbs.twimg.com/profile_images/777188003445739521/t5GNGfAc_400x400.jpg',
                 'content': str(post['text'])+'\n'+post['image']
             }
            if str(post['image'])=='None':
                data = {
                'username': 'Routiney',
                'avatar_url': 'https://pbs.twimg.com/profile_images/777188003445739521/t5GNGfAc_400x400.jpg',
                 'content': str(post['text'])
             }             

            response = requests.post('https://discord.com/api/webhooks/XXX/XXX-XXX', data=data)
            last=str(post['time'])
            f = open("r.txt", "a")
            f.write(last)
            f.close()
            #sleep(120)
    ok()
            #break;
            #sys.out(response.text)     
            #sleep(1)
                 
def ok():
    #sleep(120)
    print('WORKEDDDD !!!!!!')
    
routiney()
