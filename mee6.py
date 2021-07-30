from mee6_py_api.api import API
import discord
import sys

bot_token="bot_token_here"
server_id=000000000000000000
newbie_role_id=000000000000000000
lvl20_role_id=000000000000000000
lvl40_role_id=000000000000000000
lvl60_role_id=000000000000000000
mod_role_id=000000000000000000

intents = discord.Intents().all()

c = discord.Client(intents=intents)

@c.event
async def on_ready():
    print('ready')
    mee6API = API(server_id)
    pksz=c.get_guild(server_id)
    newbie = pksz.get_role(newbie_role_id)
    twenty = pksz.get_role(lvl20_role_id)
    forty = pksz.get_role(lvl40_role_id)
    sixty = pksz.get_role(lvl60_role_id)
    mod = pksz.get_role(mod_role_id)
    
    for member in pksz.members:
      if member.bot: continue
      user_level = await mee6API.levels.get_user_level(str(member.id), page_count_limit=1)
      if(user_level==None or user_level<20):
        await member.add_roles(newbie)
      elif(40>int(user_level)>=20):
        await member.add_roles(twenty)
        await member.remove_roles(newbie)
      elif(60>int(user_level)>=40):
        await member.add_roles(forty)
        await member.remove_roles(newbie)
        await member.remove_roles(twenty)
      elif(100>int(user_level)>=60):
        await member.add_roles(sixty)
        await member.remove_roles(newbie)
        await member.remove_roles(twenty)
        await member.remove_roles(forty)
      else:
        await member.add_roles(mod)
        await member.remove_roles(newbie)
        await member.remove_roles(twenty)
        await member.remove_roles(forty)
        await member.remove_roles(sixty)
    sys.exit()
c.run(bot_token)
