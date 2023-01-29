from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import requests

blob = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"
r=requests.get(blob, timeout=20).json()
hooks=r['hooks']

webhook = DiscordWebhook(url=hooks, username="Routiney",avatar_url="https://i.imgur.com/tQOuMXT.png",rate_limit_retry=True)

embed = DiscordEmbed(description='**stuffs:** and more stuffs ',color='e14044')
embed.set_author(name='Routine of Nepal banda', url='https://facebook.com/officialroutineofnepalbanda/posts/XXXXXXXXXXXXXXXX', icon_url='https://i.ibb.co/jvY8NK2/ronb.png')
embed.set_image(url='https://i.ibb.co/XXXXXXX/Capture.png')

webhook.add_embed(embed)
response = webhook.execute()
