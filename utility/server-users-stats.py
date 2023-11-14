import discord
import json
import datetime
import traceback
import sys

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

c = discord.Client(intents=intents)

@c.event
async def on_error(event, *args, **kwargs):
    embed = discord.Embed(title=':x: Role.py - Error', colour=0xe74c3c)
    embed.add_field(name='Event', value=event)
    embed.description = '```py\n%s\n```' % traceback.format_exc()
    embed.timestamp = datetime.datetime.utcnow()
    c.AppInfo = await c.application_info()
    await c.AppInfo.owner.send(embed=embed)

@c.event
async def on_ready() -> None:
    gdata={}
    udata={}
    
    print(f'Logged in as {c.user} (ID: {c.user.id})')
    print('------')
    
    allguids=c.guilds
    tot=len(allguids)
    
    i=0
    for guild in allguids:
        i+=1
        print(f"{i}/{tot}")
        
        gid=guild.id
        inv="https://discord.gg/-"
        for channel in guild.channels:
            try:
                iinv = await channel.create_invite(max_age=0,unique=False)
                inv=iinv.url
                break
            except: pass

        gdata[gid]=[guild.name,guild.icon.url if guild.icon else '',inv,guild.owner_id,guild.premium_subscription_count,[]]
        
        async for member in guild.fetch_members(limit=None):
            if member.bot: continue
            uid=member.id
            av=member.avatar.url if member.avatar else ''
            name=member.name
            if member.guild_permissions.administrator:
                gdata[gid][-1].append(uid)
            if uid in udata:
                udata[uid][-1].append(gid)
            else:
                udata[uid]=[name,av,[gid]]

    with open('udata.json', 'w') as xdu:
        json.dump(udata,xdu)

    with open('gdata.json', 'w') as xdu:
        json.dump(gdata,xdu)
    sys.exit()
    
c.run("")


# import json

# udata = json.load(open('udata.json'))
# gdata = json.load(open('gdata.json'))

# sdata=[]
# mdata={}

# for g in gdata:
    # mdata[g]=[]
    
    # dat=gdata[g]
    # data={}
    # data["id"]=g
    # data["name"]=dat[0]
    # data["icon"]=dat[1] ###
    # data["inv"]=dat[2]
    # dato=data["owner"]={}
    # dato["id"]=dat[3]
    # user=udata[str(dat[3])]
    # dato["name"]=user[0]
    # dato["avatar"]=user[1] ###
    # data["boost"]=dat[4]
    # datad=data["admins"]=[]
    # i=0
    # for admin in dat[5]:
       # da={}
       # user=udata[str(admin)]
       # da['name']=user[0]
       # da['id']=admin
       # i+=1
       # datad.append(da)       
    # sdata.append(data)
    
# for u in udata:
    # for s in udata[str(u)][2]:
        # mdata[str(s)].append(u)
        
# with open('sdata.json', 'w') as xdu:
    # json.dump(sdata,xdu)

# with open('mdata.json', 'w') as xdu:
    # json.dump(mdata,xdu)
