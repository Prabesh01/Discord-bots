from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import requests

blob = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"
r=requests.get(blob, timeout=20).json()
hooks=r['hooks']

#webhook = DiscordWebhook(url=hooks, username="Routiney",avatar_url="https://i.imgur.com/tQOuMXT.png",rate_limit_retry=True)
webhooks = DiscordWebhook.create_batch(urls=hooks, username="Routiney",avatar_url="https://i.imgur.com/tQOuMXT.png",rate_limit_retry=True)

embed = DiscordEmbed(description='**Breaking News: Nepal Government to Ban Discord!** \nThe government of Nepal has announced that it will soon be imposing a ban on the popular communication platform, Discord. According to the concerned authority, Government is taking this action after discord denied to comply with national policies regarding tax and social media regulations. Some officials have also expressed concern that Discord is being used for pornographic contents and cyberbullying which raises moral concerns. ||April 1st mfker||',color='e14044')
embed.set_author(name='Routine of Nepal banda', url='https://www.facebook.com/114269511553283_152326627762641', icon_url='https://i.ibb.co/jvY8NK2/ronb.png')
embed.set_image(url='https://i.ibb.co/qgmvkr3/dcban.jpg')

ilen=len(webhooks)
for i, webhook in enumerate(webhooks, start=1):
    print(f"{i}/{ilen}")
    webhook.add_embed(embed)
    response = webhook.execute()
