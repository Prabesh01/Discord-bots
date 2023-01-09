import discord
import sys

DISCORD_TOKEN = ""

intents = discord.Intents(members=True,guilds=True)#, messages=True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print('ready')
    for guild in bot.guilds:
        if guild.id==1062018654138548314:
            for channel in guild.channels:
                try:
                    link=await channel.create_invite(max_age = 0)
                    break
                except:
                    link='https://discord.gg/-'
                    pass
            print(link)
            sys.exit()
    print('no found')
    sys.exit()

bot.run(DISCORD_TOKEN)
