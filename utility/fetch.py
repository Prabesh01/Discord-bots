import discord
from os import path
import logging
import pandas as pd
logging.basicConfig(level=logging.INFO)

intents = discord.Intents(members=True,guilds=True, messages=True)#, guilds=True

c = discord.Client(intents=intents)

# intents.typing = True
# intents.presences = True
#intents.members=True
guild_count=0
@c.event
async def on_ready():
    for guild in c.guilds:
        #if(str(guild.id)!='751702370542551143'):
        #    continue
        data = pd.DataFrame(columns=['time', 'author','channel','content','attatchment','embed'])
        file_location = str(guild.id)+".csv"
        data.to_csv(file_location, index=False)
        with open(str(guild.id)+".txt", "a", encoding='utf-8') as info:
            info.write("=> "+str(guild.id)+" (name: "+str(guild.name)+')\n')
            info.write('Members:\n')
        mem_count=0
        async for member in guild.fetch_members(limit=None):
            with open(str(guild.id)+".txt", "a", encoding='utf-8') as info:
                info.write(str(mem_count)+". "+ str(member)+" - "+str(member.id)+'\n')
            mem_count = mem_count + 1
        cha_count=0
        with open(str(guild.id)+".txt", "a") as info:
            info.write('\n')
        try:
            for channel in guild.channels:
                with open(str(guild.id)+".txt", "a", encoding='utf-8') as info:
                    info.write(str(cha_count)+". "+ str(channel) +" - "+str(channel.id) +" : "+str(channel.type)+"\n")
                if(str(channel.type)=='text'):
                    try:
                        async for msg in channel.history(limit=10000000000000000000000000):
                            if msg.author == c.user:
                                    continue
                            if msg.author.bot: continue
                            # data = [
                                # [msg.created_at.isoformat(),msg.author, channel,  msg.content]# msg.embeds[0].to_dict()
                            # ]
                            embe=[]
                            embeds = msg.embeds
                            for embed in embeds:
                                embe.append(str(embed))
                            try:
                                attachment_url = msg.attachments[0].url
                                # file_request = requests.get(attachment_url)
                                # print(file_request.content)    
                            except:
                                attachment_url=''
                            data = data.append({'time': msg.created_at.isoformat(),
                                                'author': msg.author,
                                                'channel': channel,
                                                'content': msg.content,
                                                'attatchment': attachment_url,
                                                'embed': embe}, ignore_index=True)

                            # datta.append(data)
                        # #print(str(data))
                        # dataframe = pd.DataFrame(data)
                        # dataframe=dataframe.iloc[::-1]
                        # file_location = str(guild.id)+".csv"
                        # dataframe.to_csv(file_location, index=False, mode='a', header=False)              
                    except:
                        print('No history perm')
                cha_count = cha_count + 1
            # try:
                # link = await channel.create_invite(max_age = 0)
            # except:
                # link='No perms'
            # with open(str(guild.id)+".txt", "a", encoding='utf-8') as info:
                # info.write("\nInvite link: "+str(link))
            # info.close()         
            data=data.iloc[::-1]
            data.to_csv(str(guild.id)+'.csv', index=False)
            #
        except:
            pass
        guild_count = guild_count + 1
        print(guild_count)
    print('done')

c.run('TOKEN_HERE')

