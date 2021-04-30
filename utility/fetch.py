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

@c.event
async def on_ready():
    guild_count = 0
    for guild in c.guilds:
        print(guild_count)    
        data = pd.DataFrame(columns=['time', 'author','channel','content'])
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
                    async for msg in channel.history(limit=10000000000000000000000000):
                        if msg.author == c.user:
                                continue
                        if msg.author.bot: continue
                        # data = [
                            # [msg.created_at.isoformat(),msg.author, channel,  msg.content]# msg.embeds[0].to_dict()
                        # ]
                        try:
                            data = data.append({'time': msg.created_at.isoformat(),
                                                'author': msg.author,
                                                'channel': channel,
                                                'content': msg.content,
                                                'embed': msg.embeds[0].to_dict()["url"]}, ignore_index=True)
                        except:                        
                            data = data.append({'time': msg.created_at.isoformat(),
                                                'author': msg.author,
                                                'channel': channel,
                                                'content': msg.content}, ignore_index=True)
                        # datta.append(data)
                    # #print(str(data))
                    # dataframe = pd.DataFrame(data)
                    # dataframe=dataframe.iloc[::-1]
                    # file_location = str(guild.id)+".csv"
                    # dataframe.to_csv(file_location, index=False, mode='a', header=False)              
                cha_count = cha_count + 1
            # link = await channel.create_invite(max_age = 0)
            # with open(str(guild.id)+".txt", "a", encoding='utf-8') as info:
                # info.write("\nInvite link: "+str(link))
            # info.close()         
            data=data.iloc[::-1]
            data.to_csv(str(guild.id)+'.csv', index=False)
            guild_count = guild_count + 1
        except:
            pass
    print('done')

c.run('TOKEN_HERE')

