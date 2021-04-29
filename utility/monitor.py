import discord
from dotenv import load_dotenv
import os
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents(members=True,guilds=True)#, messages=True

# intents.typing = True
# intents.presences = True
#intents.members=True
 
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"=> {guild.id} (name: {guild.name})")
		print('Members:')
		mem_count=0
		async for member in guild.fetch_members(limit=None):
		    print("{}. {} - {}".format(mem_count,member,member.id))
	            mem_count = mem_count + 1
		print('')		
		guild_count = guild_count + 1

	print("Yor bot is in " + str(guild_count) + " guilds.")

bot.run(DISCORD_TOKEN)
