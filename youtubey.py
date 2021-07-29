import requests
import re
import sys
import json
import os.path
from os import path
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook, DiscordEmbed

wurl="Webhook_url_here"
useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
apikey="YT_API_KEY_HERE"
authheader="Authorization_header_here"
psid=" __Secure-3PSID VALUE HERE"
papisid="__Secure-3PAPISID Value Here"

def fl(name):
    if path.exists(name) !=True:
        f = open(name, "a")
        f.close()


cookies = {
    '__Secure-3PSID': psid,
    '__Secure-3PAPISID': papisid,
}

headers = {
    'Content-Type': 'application/json',
    'User-Agent': useragent,
    'Authorization': authheader,
    'X-Goog-Authuser': '1',
    'X-Origin': 'https://www.youtube.com'
}

response = requests.post('https://www.youtube.com//youtubei/v1/notification/get_notification_menu?key='+apikey, headers=headers, cookies=cookies, json={"context":{"client":{"clientName":"WEB","clientVersion":"2.20210224.06.00",},},"notificationsMenuRequestType":"NOTIFICATIONS_MENU_REQUEST_TYPE_INBOX"})
out=response.text
out=json.loads(out)
try:
    for i in range(20):
        try:
            vid=out['actions'][0]['openPopupAction']['popup']['multiPageMenuRenderer']['sections'][0]['multiPageMenuNotificationSectionRenderer']['items'][i]['notificationRenderer']['navigationEndpoint']['watchEndpoint']['videoId']
        except:
            vid=out['actions'][0]['openPopupAction']['popup']['multiPageMenuRenderer']['sections'][0]['multiPageMenuNotificationSectionRenderer']['items'][i]['notificationRenderer']['navigationEndpoint']['getCommentsFromInboxCommand']['videoId']
        fl('y.txt')
        f = open("y.txt", "r")
        prev=f.read()
        old=re.search(vid, prev)
        if old==None: 
            webhook = DiscordWebhook(username='Youtubey', avatar_url='https://yt3.ggpht.com/ytc/AAUvwnjF2lmkwh5hSWpkpEckEunyx1KHTC9rdWvign77vg=s88-c-k-c0x00ffffff-no-rj', url=wurl, content="https://www.youtube.com/watch?v="+vid)
            response = webhook.execute()
            f = open("y.txt", "a")
            f.write(vid+'\n')
            f.close()
    except Exception as e:
        webhook = DiscordWebhook(username='Youtubey', avatar_url='https://yt3.ggpht.com/ytc/AAUvwnjF2lmkwh5hSWpkpEckEunyx1KHTC9rdWvign77vg=s88-c-k-c0x00ffffff-no-rj', url=wurl, content="Something went wrong. Most probably, the provided values might have expired. Error:"+str(e))
        response = webhook.execute()
