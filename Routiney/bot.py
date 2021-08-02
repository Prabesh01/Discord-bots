import discord
import re
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import random
import asyncio
import json
from discord.utils import get
from discordTogether import DiscordTogether
import traceback
import datetime
import logging
import topgg
from discord.ext import tasks
import nepali_datetime
import pytz
from facebook_scraper import get_posts
from discord_webhook import DiscordWebhook, DiscordEmbed
from langdetect import detect
import time

tz_NP = pytz.timezone('Asia/Kathmandu')
now = datetime.datetime.now(tz_NP)

c = discord.Client()

togetherControl = DiscordTogether(c)

DISCORD_TOKEN = "DISCORD_BOT_TOKEN_HERE"
log = "DISCORD_WEBHOOK_URL_TO_SEND_ERROR+LOGS_TO"
myhook =  log
#EXAMPLE JSONBLOB URL:https://jsonblob.com/api/jsonBlob/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
blob = "JSONBLOB_URL_1"
blobre = "JSONBLOB_URL_2"
bloboa = "JSONBLOB_URL_3"
blobr = "JSONBLOB_URL_4"
dbl_token="TOP.GG_BOT'S_WEBHOOK_TOKEN_HERE"

c.topggpy = topgg.DBLClient(c, dbl_token, autopost=True, post_shard_count=False)


@c.event
async def on_autopost_success():
    print(
        f"Posted server count ({c.topggpy.guild_count}) to top.gg"
    )

@tasks.loop(minutes=5)
async def test():
    bin=requests.get(blobr, timeout=20).json()
    r=requests.get(blob, timeout=20).json()
    hooks=r['hooks']
    if not hooks:
        coker={'content':'JSONBLOB - STH WENT WRONG!'}
        requests.post(myhook, data=coker, timeout=20)
    print(len(hooks))
    tme=[]
    new=0
    prev=bin['r']
    for post in get_posts('officialroutineofnepalbanda', pages=1, cookies='cook.txt'):#, cookies='cook.txt'
        ptid=str(post['post_id'])
        if(str(ptid) in str(tme)):
          continue
        tme.append(ptid)
        old=re.search(str(ptid), str(prev))
        if old==None:
            new=1
            print('not old')
            pvalu=str(post['text'])
            try:
              if(detect(str(pvalu))!='en'):
                print('np')
                if(int(len(str(post['text']))>=500)):
                  outp=[(str(post['text'])[i:i+500]) for i in range(0, len(str(post['text'])), 500)]      
                  mat=str(len(str(post['text']))/500).split('.')[0]
                  pvalu='.......'+outp[int(mat)]
                  posz=0
                  for m in range(0,int(mat)):
                    webhook = DiscordWebhook(username='Routiney', avatar_url='https://i.imgur.com/tQOuMXT.png',url=hooks)#https://cdn.discordapp.com/app-icons/786534057437691914/8dd876fd77d51452a5e3b3df4bc0ce18.png?size=256
                    if(posz==0):
                      embed = DiscordEmbed(description=outp[int(m)]+'.......')
                      posz=1
                    else:
                      embed = DiscordEmbed(description='.......'+outp[int(m)]+'.......')
                    embed.set_author(name='Routine of Nepal banda', url=post['post_url'], icon_url='https://i.imgur.com/tIG8e4n.jpg')#https://pbs.twimg.com/profile_images/1382031487562784769/aQuI4Ppk_400x400.jpg
                    webhook.add_embed(embed)
                    webhook.execute()
                else:
                  pvalu=str(post['text'])
            except Exception as e:
              print(str(e))
              langer={'content':str(e)}
              requests.post(myhook, data=langer, timeout=20)
            if(str(post['video'])!='None'):
              webhook = DiscordWebhook(username='Routiney', avatar_url='https://i.imgur.com/tQOuMXT.png',url=hooks, content=pvalu+'\n<'+str(post['post_url'])+'>\n'+str(post['video']))
              webhook.execute()
              continue
            webhook = DiscordWebhook(username='Routiney', avatar_url='https://i.imgur.com/tQOuMXT.png', url=hooks)
            embed = DiscordEmbed(description=pvalu)
            embed.set_author(name='Routine of Nepal banda', url=post['post_url'], icon_url='https://i.imgur.com/tIG8e4n.jpg')
            img = post['images']
            try:
              imgcount=len(img)
              if(imgcount>2):
                webhook.add_embed(embed)
                webhook.execute()
                for imgs in post['images']:
                    webhook = DiscordWebhook(username='Routiney', avatar_url='https://i.imgur.com/tQOuMXT.png',url=hooks)
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
                #embed.set_footer(text="")
                embed.timestamp = str(post['time'].replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Kathmandu')))
                webhook.add_embed(embed)
                webhook.execute()
            except:
              embed.set_image(url=post['image'])
              embed.timestamp = str(post['time'].replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Kathmandu')))#embed.set_footer(text='Top 5 active guilds for the month of July: Anime Nepal, The Bois, emdt, हाम्रो साझा घर, 7 Deadly Sins. Congrats!\nLeaderboard available at ronb.xyz/top')
              webhook.add_embed(embed)
              webhook.execute()
                
    if not tme:
      print('For loop skipped')
    else:
      if new==1:
        print('new')
        data = {"r": tme}
        requests.put(blobr,timeout=20, data=json.dumps(data))

async def status_task():
  while True:
    await c.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="ronb.xyz"))
    await asyncio.sleep(3)
    await c.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="r!help"))
    await asyncio.sleep(3)
    noww=nepali_datetime.date.today()
    await c.change_presence(activity=discord.Game(name=noww.strftime("%D %N %K - %G")))
    await asyncio.sleep(3)
    now = datetime.datetime.now(tz_NP)
    await c.change_presence(activity=discord.Game(name=now.strftime("%d %b %Y - %a")))
    await asyncio.sleep(3)
    now = datetime.datetime.now(tz_NP)
    await c.change_presence(activity=discord.Game(name=now.strftime("%I:%M.%S %p")))
    await asyncio.sleep(3)

    
    
@c.event
async def on_ready():
    print('ready')
    if test.is_running() != True:
        test.start()
    c.loop.create_task(status_task())
    pass

@c.event
async def on_error(event, *args, **kwargs):
    embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c) #Red
    embed.add_field(name='Event', value=event)
    embed.description = '```py\n%s\n```' % traceback.format_exc()
    embed.timestamp = datetime.datetime.utcnow()
    c.AppInfo = await c.application_info()
    await c.AppInfo.owner.send(embed=embed)
        
@c.event
async def on_guild_join(guild):
    data={'content':'joined: '+str(guild.id)+' : '+str(guild.name)}
    requests.post(log, data=data)
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
          await channel.send("Use r!sub command to start receiving latest RONB posts to your server")
          member=guild.me
          perm_list = [perm[0] for perm in channel.permissions_for(member) if perm[1]]
          if not('embed_links' in perm_list):
            await channel.send("It would be great if I had permission to embed links. Anyways, here you go:\n\nr!help - Display Routiney Bot's Command List\nr!sub - Subscribe this text channel to receive new RONB posts\nr!unsub- Unsubscribe this text channel\n\n- Disable 'oa' command using 'r!oa' if slang words aren't appropritae for your server\n- Contact Prabesh#0001 if you faced any issue with the bot or join our support server: ehRSPHuTDy\n- For more info, visit https://ronb.xyz")
            return 
          embed=discord.Embed(title="r!help", description="Display Routiney Bot's Command List")
          embed.add_field(name="r!sub", value="Subscribe this text channel to receive new RONB posts", inline=False)
          embed.add_field(name="r!unsub", value="Unsubscribe this text channel", inline=False)
          embed.set_footer(text="- Disable 'oa' command using 'r!oa' if slang words aren't appropritae for your server\n- Contact Prabesh#0001 if you faced any issue with the bot or join our support server: ehRSPHuTDy\n- For more info, visit https://ronb.xyz") 
          await channel.send(embed=embed)
          break
        break

@c.event
async def on_raw_reaction_add(payload):
    user=payload.user_id
    message=payload.message_id
    channel=payload.channel_id
    guild=payload.guild_id
    emoji=payload.emoji
    member=payload.member
    if str(emoji) != "🔁":
        return
    if user == c.user.id:
        return
    guil = c.get_guild(guild)
    chan=discord.utils.get(guil.channels, id=channel)
    msz=await chan.fetch_message(message)
    #print(msz.author)
    if str(msz.author) != 'Routiney#0000':
        print('msz')
        return
    rpst=requests.get(blobre, timeout=20).json()
    if not str(guild) in str(rpst.keys()): #check if enabled
        try:
        	await chan.send('Well, repost has not been enabled in your server. Admins can use r!repost to enable it.',delete_after=5)
        except:
        	await payload.member.send("Well, repost has not been enabled in your server. Admins can use r!repost to enable it.")
        	await payload.member.send("Also I don't have permission to send message to that channel where you reacted repost 🔁.")
        return
    wurl=rpst[str(guild)]
    try:
        attachment_url = msz.attachments[0].url   
    except:
        attachment_url=''
    try:
      embe = msz.embeds[0].to_dict()
      webhook = DiscordWebhook(username=str(member.name), avatar_url=str(member.avatar_url), url=wurl, content=str(msz.content))
      embed=DiscordEmbed(title="Go to message!", url="https://discord.com/channels/"+str(guild)+"/"+str(channel)+"/"+str(message), description="**Jump**")
      webhook.add_embed(embed)
      webhook.execute()
      webhool = DiscordWebhook(username=str(member.name), avatar_url=str(member.avatar_url), url=wurl, content=str(msz.content))
      webhool.add_embed(embe)
      webhool.execute()
    
    except:
        webhook = DiscordWebhook(username=str(member.name), avatar_url=str(member.avatar_url), url=wurl)
        embe=DiscordEmbed(description=str(msz.content))
        embe.set_author(name=str(msz.author.name), url="https://discord.com/channels/"+str(guild)+"/"+str(channel)+"/"+str(message), icon_url=str(msz.author.avatar_url))
        embe.add_embed_field(name="\u200b", value="[Go to message!](https://discord.com/channels/"+str(guild)+"/"+str(channel)+"/"+str(message)+")", inline=False)
        embe.set_image(url=attachment_url)
        webhook.add_embed(embe)
        webhook.execute()

emojis = ['👍', '👎', '❤️', '🔁']

@c.event
async def on_message(message):
    if str(message.author) == 'Routiney#0000':
        try:
          for emoji in emojis:
              await message.add_reaction(emoji)
        except:
          pass        
        return
    if message.author == c.user:
            return
    if message.author.bot: return    

    if message.content.startswith("oa ") or message.content == 'oa':
        oabin=requests.get(bloboa).json()
        if message.channel.id==788423186546819083:
            return
        try:
          if(str(message.guild.id) in str(oabin['oa'])):
            if message.content == 'oa':
                try:
                    await message.channel.send('Command disabled by your sadist server admin')
                except:
                    try:
                        await message.author.send("I don't have permission to send message in that channel")
                    except:
                        c.AppInfo = await c.application_info()
                        await c.AppInfo.owner.send(str(message.author)+' from '+str(message.guild)+' ('+str(message.guild.id)+') - oa sadist admin')
            return
        except:
            pass
        oa = [
        'Chup mug',
        'disturb vo mug',
        'https://media.tenor.com/images/ee616b63bab2fa326e867f452235894a/tenor.gif',
        'guu kha mug 💩',
        'https://i.imgur.com/M3OhyYn.jpg',
        'lyang lyang na han na lado',
        '<:muji:864716123500183611>',
        'https://media.tenor.com/images/8e834a7c1807ac17265c11071b1c5748/tenor.gif',
        'jurukka uthera jhyamma mukh padkau!',
        'Sutna dyao, chuppa lara!',
        'marna nasakyo randi ko xoro muji',
        'https://media.tenor.com/images/4da49d51af9f989e520080b7557e050c/tenor.gif',
        'aade paade, malai bolaune teri ma lwan tate vate kya ho?',
        'bhutro khojeko ho muji?',
        'thukka machikne randiko xoroharu',
        'randiko xoro bahun machikne',
        'Naak katdim ta mug newarko?',
        'Turi tandim tero?',
        'kasto muji gula jasto raixa chikne',
        'https://media.tenor.com/images/fa8ceb000dad3a6b5d34fdc002530715/tenor.gif',
        'class ma jaa chikne. tero mom lai vandim?',
        'k vo mug?',
        'yo muji ko ho feri?',
        'jaa mug tiktok bana. k discord chalauxas ta',
        'khate bahun',
        'https://media.tenor.com/images/473f1d3b5df4ce28d7ce53ffd8bfd9bd/tenor.gif',
        'lati ko poi'
        ]
        response = random.choice(oa)
        try:
        	await message.channel.send(response)
        except:
            await message.author.send('I don\'t have permission to send messages to the channel.')
        return

    if message.guild is None:
        await message.channel.send("Only oa command can be used from DM.\nFor support regarding the bot, visit <https://ronb.xyz> or contact Prabesh#0001 or join the support server:\nhttps://discord.com/invite/ehRSPHuTDy")
        return
    
    if message.content=='r!repost':
      if message.author.guild_permissions.administrator:
          pass
      else:
          try:
          	await message.channel.send("Only server admins are allowed to use this command!")
          except:
          	await message.author.send("Only server admins are allowed to use this command!\nAlso I don't have permission to send message in that channel so consider giving me the permission.")
          return
      member=message.guild.me
      perm_list = [perm[0] for perm in message.channel.permissions_for(member) if perm[1]]
      if not('send_messages' in perm_list):
        try:
        	await message.author.send("lmao. I don't have permission to send message in that channel")
        except:
        	c.AppInfo = await c.application_info()
        	await c.AppInfo.owner.send(str(message.author)+' from '+str(message.guild)+' ('+str(message.guild.id)+') - r!repost')
        return
      if not('manage_webhooks' in perm_list):
        await message.channel.send("You must provide me permission to manage webhooks in order to use this command.")
        return
      if not('embed_links' in perm_list):
        await message.channel.send("You must provide me permission to embed links in order to use this command.")
        return 
      if not('read_message_history' in perm_list):
        await message.channel.send("You must provide me permission to read message history in order to use this command.")
        return
      if not('manage_messages' in perm_list):
        await message.channel.send("You must provide me permission to manage messages in order to use this command.")
        return
      rpst=requests.get(blobre).json()
      if str(message.guild.id) in rpst.keys():
        for hook in await message.channel.webhooks():
          if hook.name == 'Routiney repost':
            try:
              await hook.delete()
            except:
              pass
        rpst.pop(str(message.guild.id))
        requests.put(blobre, data=json.dumps(rpst))
        await message.channel.send('Sucessfully disabled Repost in this server\nUse r!repost in any channel where you want members to be able to repost Routiney\'s messages; mostly a chat channel where a member can talk about the news with others')
  

      else:
          web=await message.channel.create_webhook(name='Routiney repost')
          rpst[message.guild.id] = web.url
          requests.put(blobre, data=json.dumps(rpst))
          await message.channel.send('Repost enabled!\nWhenever a member reacts repost in Routiney\'s messages, the messages will be reposted here.\nNews channel are mostly muted by everyone, so if a member wants to talk about a news in another channel, this feature comes in handy\nUse r!repost to disable this')

    if message.content == 'r!yt':
      if message.author.guild_permissions.administrator:
          pass
      else:
          await message.channel.send("Only server admins are allowed to use this command!")
          return
      try:
        link = await togetherControl.create_link(message.author.voice.channel.id, 'youtube')
        await message.channel.send(f"<{link}>")
      except:
        await message.channel.send("Make sure you are connected to a voice channel before using this command and bot has permission to view, connect and create invite link in both the text channel and voice channel\n\nThis is beta feature so problems might arise, inform Prabesh#0001")

    if message.content == 'r!chess':
      if message.author.guild_permissions.administrator:
          pass
      else:
          await message.channel.send("Only server admins are allowed to use this command!")
          return
      try:
        link = await togetherControl.create_link(message.author.voice.channel.id, 'chess')
        await message.channel.send(f"<{link}>")
      except:
        await message.channel.send("Make sure you are connected to a voice channel before using this command and bot has permission to view, connect and create invite link in both the text channel and voice channel\n\nThis is beta feature so problems might arise, inform Prabesh#0001")

    if message.content == 'r!poker':
      if message.author.guild_permissions.administrator:
          pass
      else:
          await message.channel.send("Only server admins are allowed to use this command!")
          return
      try:
        link = await togetherControl.create_link(message.author.voice.channel.id, 'poker')
        await message.channel.send(f"<{link}>")
      except:
        await message.channel.send("Make sure you are connected to a voice channel before using this command and bot has permission to view, connect and create invite link in both the text channel and voice channel\n\nThis is beta feature so problems might arise, inform Prabesh#0001")

    if message.content == 'r!betrayal':
      if message.author.guild_permissions.administrator:
          pass
      else:
          await message.channel.send("Only server admins are allowed to use this command!")
          return
      try:
        link = await togetherControl.create_link(message.author.voice.channel.id, 'betrayal')
        await message.channel.send(f"<{link}>")
      except:
        await message.channel.send("Make sure you are connected to a voice channel before using this command and bot has permission to view, connect and create invite link in both the text channel and voice channel\n\nThis is beta feature so problems might arise, inform Prabesh#0001")

    if message.content == 'r!fishing':
      if message.author.guild_permissions.administrator:
          pass
      else:
          await message.channel.send("Only server admins are allowed to use this command!")
          return
      try:
        link = await togetherControl.create_link(message.author.voice.channel.id, 'fishing')
        await message.channel.send(f"<{link}>")
      except:
        await message.channel.send("Make sure you are connected to a voice channel before using this command and bot has permission to view, connect and create invite link in both the text channel and voice channel\n\nThis is beta feature so problems might arise, inform Prabesh#0001")

    if message.content == "r!":
        member=message.guild.me
        perm_list = [perm[0] for perm in message.channel.permissions_for(member) if perm[1]]
        if not('send_messages' in perm_list):
          try:
          	await message.author.send("lmao. I don't have permission to send message in that channel")
          except:
          	c.AppInfo = await c.application_info()
          	await c.AppInfo.owner.send(str(message.author)+' from '+str(message.guild)+' ('+str(message.guild.id)+') is dumb af - r!')
          return
        if not('manage_webhooks' in perm_list):
          await message.channel.send("Grrrr. I don't have permission to manage webhooks. You must provide me that permission in order to use me.")
          return
        if not('embed_links' in perm_list):
          await message.channel.send("Grrrr. I don't have permission to embed links. I would need that permission to show you images, videos and a neat help message. This permission isn't compulsory but highly recommended.\nEverything else seems fine.")
          return 
        if not('read_message_history' in perm_list):
          await message.channel.send("I don't have permission to read message history. This permisson isn't compulsory but you won't be able to use the repost feature or use // command.\nEverything else seems fine.")
          #\nFor more information, contact: Prabesh#1134
          return
        if not('manage_messages' in perm_list):
          await message.channel.send("I don't have permission to manage messages of this channel. This permisson isn't compulsory but you won't be able to use the repost feature or use // command.\nEverything else seems fine.")#\nFor more information, contact: Prabesh#1134
          return
        if not('add_reactions' in perm_list):
          await message.channel.send("I don't have permission to add reactions to messages of this channel. This permisson isn't compulsory but you won't be able to use the repost feature.\nEverything else seems fine.")#\nFor more information, contact: Prabesh#1134
          return

        if('administrator' in perm_list):
          await message.channel.send("Everything is just perfect!\nFeel free to contact me if you face any issue: Prabesh#0001")
          return
        await message.channel.send("Looks like you set me up well\nFeel free to contact me if you face any issue: Prabesh#0001")

    if message.content == 'r!help':
      member=message.guild.me
      perm_list = [perm[0] for perm in message.channel.permissions_for(member) if perm[1]]
      if not('send_messages' in perm_list):
        try:
         await message.author.send("lmao. I don't have permission to send message in that channel")
        except:
         c.AppInfo = await c.application_info()
         await c.AppInfo.owner.send(str(message.author)+' from '+str(message.guild)+' ('+str(message.guild.id)+') - r!help')
        return
      if not('embed_links' in perm_list):
        await message.channel.send("It would be great if I had permission to embed links. Anyways, here you go:\n\nr! - Check if the bot is feeling comfortable in your server\nr!sub - Subscribe this text channel to receive new RONB posts\nr!unsub- Unsubscribe this text channel\nr!invite - Get bot's invite link\nr!faq- See FAQs\noa- Fun command \nr!oa- Enable/disable oa command\n//- Delete messages of this channel\nr!repost- Enable/disable repost feature\n\nContact Prabesh#0001 if you faced any issue with the bot\nSupport Server: ehRSPHuTDy")
        return 
      embed=discord.Embed(title="r!help", description="Display Routiney Bot's Command List")
      embed.add_field(name="r!", value="Check if the bot is feeling comfortable in your server", inline=False)
      embed.add_field(name="r!sub", value="Subscribe this text channel to receive new RONB posts", inline=False)
      embed.add_field(name="r!unsub", value="Unsubscribe this text channel", inline=False)
      embed.add_field(name="r!invite", value="Get bot's invite link", inline=False)
      embed.add_field(name="r!faq", value="See FAQs", inline=False)
      embed.add_field(name="oa", value="Fun command", inline=False)
      embed.add_field(name="r!oa", value="Enable/disable oa command", inline=False)      
      embed.add_field(name="r!repost", value="Enable/Disable repost feature", inline=False)
      embed.set_footer(text="Contact Prabesh#0001 if you faced any issue with the bot\nSupport Server: ehRSPHuTDy")
      await message.channel.send(embed=embed)

    if message.content == 'r!faq':
      member=message.guild.me
      perm_list = [perm[0] for perm in message.channel.permissions_for(member) if perm[1]]
      if not('send_messages' in perm_list):
        try:
         await message.author.send("I don't have permission to send message in that channel")
        except:
         c.AppInfo = await c.application_info()
         await c.AppInfo.owner.send(str(message.author)+' from '+str(message.guild)+' ('+str(message.guild.id)+') - r!faq')
        return 
      if not('embed_links' in perm_list):
        await message.channel.send("You must gimme embed links permission to se FAQs")
        return 
      embed=discord.Embed()
      embed.add_field(name="RONB ko official bot ho?", value="haina", inline=False)
      embed.add_field(name="post ko link pani send gare ramro hunthyo", value="post mathi Routine of Nepal banda lekheko ma click", inline=False)
      embed.add_field(name="Bot ko source code?", value="https://github.com/Prabesh01/Discord-bots/", inline=False)
      embed.add_field(name="How many servers are using this bot?", value="As of now, "+str(len(c.guilds))+" servers have this bot.", inline=False)
      embed.add_field(name="How to donate?", value="chaidaina", inline=False)
      embed.add_field(name="Some messages are splitted, why?", value="Eutai message ma 500 vanda badi nepali characters vayo vane discord le last tira ko words ko aakar ukar faldido raixa. So long nepali posts are divided into multiple messages.\nMore info: https://support.discord.com/hc/en-us/community/posts/1500001279881", inline=False)
      embed.add_field(name="Known issues?", value="- kaile kai post dheelo auxa | facebook le request block garxa kaile kai\n- video pathauda laamo link pani aauxa | tyo laamo link napathai video embed nai hudaina discord ma\n- purano posts ko video chaldaina | facebook le video ko temporary  url deko hunxa jun 1 2 din paxi expire hunxa", inline=False)#- kaile kai bot down hunxa | can't help, its free hosting\n- kaile kai eutai post 2 3 patak aauxa | not sure why that happens\n
      embed.add_field(name="गजब छ बा kasari taneko?", value="English ma dinxu hai. This bot everyday goes to ekantipur's epaper site and fetches its first page. Then, it looks for गजब छ बा! using a Computer Vision library (opencv-python) and if available, it crops the required part and sends to everyone.", inline=False)
      embed.add_field(name="Yesari scrape gareko illegal hoina?", value="ho", inline=False)
      embed.set_footer(text="Contact Prabesh#0001 if you faced any issue with the bot\nSupport Server: ehRSPHuTDy")
      await message.channel.send(embed=embed)

    if message.content == 'r!oa':
      if message.author.guild_permissions.administrator:
          pass
      else:
          try:
          	await message.channel.send("Only server admins are allowed to use this command!")
          except:
          	await message.author.send("I don't have permission to send message in that channel!")
          return
      oabin=requests.get(bloboa).json()
      if(str(message.guild.id) in str(oabin['oa'])):
        oalistb=[]
        try:
          for pieceb in oabin['oa']:
            if(str(pieceb)!=str(message.guild.id)):
              oalistb.append(pieceb)
        except:
              datalistb={'oa':''}
              requests.put(bloboa, data=json.dumps(datalistb))
              oabin=requests.get(bloboa).json()        
        oabin['oa']=oalistb
        requests.put(bloboa, data=json.dumps(oabin))
        try:
        	await message.channel.send('oa command enabled sucessfully')
        except:
        	await message.author.send('I don\'t have permission to send messages in that channel\noa command has been enabled tho.')
      else:
        oalista=[]
        try:
          for piecea in oabin['oa']:
              oalista.append(piecea)
        except:
              datalista={'oa':''}
              requests.put(bloboa, data=json.dumps(datalista))
              oabin=requests.get(bloboa).json()
        oalista.append(str(message.guild.id))
        oabin['oa']=oalista
        requests.put(bloboa, data=json.dumps(oabin))
        try:
        	await message.channel.send('oa command disabled sucessfully')
        except:
        	await message.author.send('I don\'t have permission to send messages in that channel.\noa command has been disabled tho')


    if message.content == 'r!invite':
        try:
        	await message.channel.send('<https://ronb.xyz/invite>')#('<https://discord.com/api/oauth2/authorize?client_id=786534057437691914&permissions=536963072&scope=bot>'\n\n<https://top.gg/bot/786534057437691914#/>\n<https://botsfordiscord.com/bot/786534057437691914>')
        except:
        	await message.author.send('I don\'t have permission to send mesasge in that channel.\nAnyway, here you go: <https://ronb.xyz/invite>')


    if message.content == 'r!sub':
        if message.author.guild_permissions.administrator:
            pass
        else:
            await message.channel.send("Only server admins are allowed to use this command!")
            return
        member=message.guild.me
        perm_list = [perm[0] for perm in message.channel.permissions_for(member) if perm[1]]
        if not('send_messages' in perm_list):
          try:
          	await message.author.send("I don't have permission to send message in that channel")
          except:
          	c.AppInfo = await c.application_info()
          	await c.AppInfo.owner.send(str(message.author)+' from '+str(message.guild)+' ('+str(message.guild.id)+') - r!sub')
          return
        if not('manage_webhooks' in perm_list):
          await message.channel.send("Grrrr. I don't have permission to manage webhooks. You must provide me that permission in order to use me.")
          return  
        bin=requests.get(blob).json()
        #bin=bin['record']
        hooks=bin['hooks']
        channl=bin['channel']
        clts = message.channel.id
        channel = c.get_channel(clts)
        clts=str(clts)
        prev=str(channl)
        old=re.search(clts, prev)
        if old==None:
            channl.append(clts)
            web=await channel.create_webhook(name='Routiney')
            clt=web.url
            data={'content':'subd: '+str(clts)+' : '+str(clt)}
            requests.post(log, data=data)
            hooks.append(clt)
            bin['hooks']=hooks
            bin['channel']=channl
            requests.put(blob, data=json.dumps(bin))
            await message.channel.send("This channel is subscribed to receive routiney's new shit. Wait till RONB posts any new post.\nUse r!unsub to unsubscribe\nFeel free to contact me if you face any issue: Prabesh#0001")
        if old!=None:
            await message.channel.send("This channel was already subscribed. \n Use r!unsub to unsubscribe first.")

    if message.content == 'r!unsub':
        if message.author.guild_permissions.administrator:
            pass
        else:
            await message.channel.send("Only server admins are allowed to use this command!")
            return  
        bin=requests.get(blob).json()
        hooks=bin['hooks']
        channl=bin['channel']
        clts = message.channel.id
        clt=str(clts)
        prev=str(channl)
        old=re.search(clt, prev)
        if old!=None:
            for hook in await message.channel.webhooks():
                hoo=re.sub(r'\D','',str(hook))
                for t in hooks:
                    if hoo in t:
                        await hook.delete()
                        hooks.remove(t)        
                        data={'content':'unsubd: '+str(clt)+' : '+str(t)}
                        requests.post(log, data=data)
            for a in channl:
                if clt in a:
                  channl.remove(a) 
            bin['hooks']=hooks
            bin['channel']=channl
            requests.put(blob, data=json.dumps(bin))
            try:    
            	await message.channel.send("This channel is unsubscribed sucessfully\nFeel free to send me your feedbacks/complaints: Prabesh#0001")
            except:
            	try:
                	await message.author.send("That channel is unsubscribed sucessfully\nFeel free to send me your feedbacks/complaints: Prabesh#0001\n\nAlso, I don't have permission to send message in that channel")
            	except:
                	c.AppInfo = await c.application_info()
                	await c.AppInfo.owner.send(str(message.author)+' from '+str(message.guild)+' ('+str(message.guild.id)+') - r!unsub')
        if old==None:
            try:
            	await message.channel.send("This channel was never subscribed\nUse r!sub to subscribe")
            except:
            	try:
                	await message.author.send("I don't have permission to send message in that channel")
            	except:
                	c.AppInfo = await c.application_info()
                	await c.AppInfo.owner.send(str(message.author)+' from '+str(message.guild)+' ('+str(message.guild.id)+') - r!unsub never sunscribe')


    if message.content == '//':
        if message.author.guild_permissions.administrator:
            pass
        else:
            await message.channel.send("Only server admins are allowed to use this command!")
            return
        member=message.guild.me
        perm_list = [perm[0] for perm in message.channel.permissions_for(member) if perm[1]]
        if not('send_messages' in perm_list):
          try:
          	await message.author.send("I don't have permission to send message in that channel")
          except:
          	c.AppInfo = await c.application_info()
          	await c.AppInfo.owner.send(str(message.author)+' from '+str(message.guild)+' ('+str(message.guild.id)+') is dumb af - //')
          return
        if not('read_message_history' in perm_list):
          await message.channel.send("uh oh, Looks like I don't have permission to read message history. Provide me the permission in order to use this command.")
          return
        if not('manage_messages' in perm_list):
          await message.channel.send("uh oh, Looks like I don't have permission to manage messages of this channel. Provide me the permission in order to use this command.")
          return
        #if message.author.id==736529187724197951:
        #  pass
        #else:
        #  await message.channel.send("Command depreciated. No longer available :(")
        #  return
        try:    
          await message.channel.send("Deleting messages of this channel in 5 seconds..")
          #await message.channel.send("If you mistakely entered this command, hehe I can do nothing now.")
          await asyncio.sleep(5)
          await message.channel.purge(limit=None, check=lambda msg: not msg.pinned)
          #async for msg in message.channel.history(limit=10000000000000000000000000):
              #await msg.delete()
        except:
          #pass
          await message.channel.send("uh oh, Looks like I don't have enough permission. Make sure I have permission to manage messages and read message history in the channel.")      
c.run(DISCORD_TOKEN)
