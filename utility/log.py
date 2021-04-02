import discord
from os import path
#import logging
import pandas as pd
#logging.basicConfig(level=logging.INFO)

c = discord.Client()

@c.event
async def on_message(message):
    if message.author == c.user:
            return
    if message.author.bot: return
    clts = message.channel.id
    channel = c.get_channel(clts)
    ID = message.guild.id
    guild = c.get_guild(ID)
    data = pd.DataFrame(columns=['time', 'author','guild','channel','content'])
    if path.exists(str(ID)+'.csv') !=True:
        async for msg in message.channel.history(limit=10000000000000000000000000):
            if msg.author == c.user:
                    continue
            if msg.author.bot: continue            
            data = data.append({'time': msg.created_at.isoformat(),
                                'author': msg.author,
                                'guild': guild,
                                'channel': channel,
                                'content': msg.content}, ignore_index=True)
        data=data.iloc[::-1]
        file_location = str(ID)+".csv"
        data.to_csv(file_location, index=False)
        #print('done')
    else:
        data = [
            [message.created_at.isoformat(),message.author.name, guild, channel,  message.content]
        ]
        dataframe = pd.DataFrame(data)
        dataframe.to_csv(str(ID)+".csv", index=False, mode='a', header=False)
        #print('dups')
    
c.run('TOKEN_HERE')
