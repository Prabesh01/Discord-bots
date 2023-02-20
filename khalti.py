import interactions
import requests
import pymongo
import config
import json
import base64
from Crypto.Cipher import AES # pycryptodome noy pycrypto
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import datetime
 
client = pymongo.MongoClient()
#client = pymongo.MongoClient('mongodb://%s:%s@%s' % (config.mongo_user, config.mongo_pass, config.mongo_host))

dblist = client.list_database_names()
if "khalti" in dblist:
    db = client.khalti
else:
    db = client["khalti"]
collection = db['users']

temp_otp_token={}

bot = interactions.Client(token=config.bot_token)

bot.load('interactions.ext.files')

@bot.event
async def on_ready():
    print("App started")

@bot.command(
    name="khalti",
    description="Interact with your khalti account",
    options=[
        interactions.Option(
            name="login",
            description="Login to a khalti account.",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
               interactions.Option(
                 name="username",
                 description="Khalti Mobile or Email",
                 type=interactions.OptionType.STRING,
                 required=True
               ),
               interactions.Option(
                 name="password",
                 description="Account Password",
                 type=interactions.OptionType.STRING,
                 required=True
               ),                              
               interactions.Option(
                 name="master_key",
                 description="Create a easy to remember password. You will need this key to perform any transactions in future.",
                 type=interactions.OptionType.STRING,
                 required=True
               )
            ]
        ),
        interactions.Option(
            name="otp",
            description="OTP verification",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
               interactions.Option(
                 name="code",
                 description="Enter the OTP Code you received from Khalti",
                 type=interactions.OptionType.INTEGER,
                 required=True
               ),                              
               interactions.Option(
                 name="repeat_master_key",
                 description="Re-enter you master key to make sure you remember it cuz master key cant be recovered at all.",
                 type=interactions.OptionType.STRING,
                 required=True
               )
            ]            
        ),
        interactions.Option(
            name="info",
            description="Get your khalti account info",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
               interactions.Option(
                 name="master_key",
                 description="Enter the master password you created when logging in.",
                 type=interactions.OptionType.STRING,
                 required=True
               )
            ]
        ),
        interactions.Option(
            name="qr",
            description="Get your QR code to receive payments",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
               interactions.Option(
                 name="master_key",
                 description="Enter the master password you created when logging in.",
                 type=interactions.OptionType.STRING,
                 required=True
               )
            ]
        ),
        interactions.Option(
            name="balance",
            description="Check your khalti account balance",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
               interactions.Option(
                 name="master_key",
                 description="Enter the master password you created when logging in.",
                 type=interactions.OptionType.STRING,
                 required=True
               ),               
               interactions.Option(
                 name="hide_message",
                 description="Default: True [hides message]",
                 type=interactions.OptionType.BOOLEAN,
                 required=False,
               )
            ]
        ),
        interactions.Option(
            name="history",
            description="View your last 5 transactions",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
               interactions.Option(
                 name="master_key",
                 description="Enter the master password you created when logging in.",
                 type=interactions.OptionType.STRING,
                 required=True
               ),               
               interactions.Option(
                 name="hide_message",
                 description="Default: True [hides message]",
                 type=interactions.OptionType.BOOLEAN,
                 required=False,
               )
            ]
        ),
        interactions.Option(
            name="transfer",
            description="Send amount to other khalti user.",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
               interactions.Option(
                 name="khalti_id",
                 description="Enter Khalti Mobile or Email of the receiver",
                 type=interactions.OptionType.STRING,
                 required=True
               ),
               interactions.Option(
                 name="amount",
                 description="enter amount to send",
                 type=interactions.OptionType.INTEGER,
                 required=True
               ),                              
               interactions.Option(
                 name="master_key",
                 description="Create a easy to remember password. You will need this key to perform any transactions in future.",
                 type=interactions.OptionType.STRING,
                 required=True
               ),                              
               interactions.Option(
                 name="purpose",
                 description="Default: Personal Use",
                 type=interactions.OptionType.STRING,
                 required=False,
                 choices=[
                  interactions.Choice(
                    name="personal_use",
                    value="Personal Use"
                  ),
                  interactions.Choice(
                    name="Borrow_Lend",
                    value="Borrow/Lend"
                  ),
                  interactions.Choice(
                    name="family_expenses",
                    value="Family Expenses"
                  ),
                  interactions.Choice(
                    name="bill_sharing",
                    value="Bill Sharing"
                  ),
                  interactions.Choice(
                    name="salary",
                    value="Salary"
                  ),
                  interactions.Choice(
                    name="others",
                    value="Others"
                  )                                    
                ]                 
               ),                              
               interactions.Option(
                 name="remarks",
                 description="Default: Transaction made through Routiney discord bot",
                 type=interactions.OptionType.STRING,
                 required=False
               ),               
               interactions.Option(
                 name="hide_message",
                 description="Default: True [hides message]",
                 type=interactions.OptionType.BOOLEAN,
                 required=False,
               )
            ]
        ),
        interactions.Option(
            name="topup",
            description="Topup a phone.",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
               interactions.Option(
                 name="number_to_topup",
                 description="Enter Mobile number to topup",
                 type=interactions.OptionType.INTEGER,
                 required=True
               ),
               interactions.Option(
                 name="amount",
                 description="enter amount to topup",
                 type=interactions.OptionType.INTEGER,
                 required=True
               ),                              
               interactions.Option(
                 name="master_key",
                 description="Create a easy to remember password. You will need this key to perform any transactions in future.",
                 type=interactions.OptionType.STRING,
                 required=True
               ),               
               interactions.Option(
                 name="hide_message",
                 description="Default: True [hides message]",
                 type=interactions.OptionType.BOOLEAN,
                 required=False,
               )
            ]
        ),
        interactions.Option(
            name="logout",
            description="Log out this discord account from khalti.",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
               interactions.Option(
                 name="master_key",
                 description="Entering master key ensures you are completely logged out.",
                 type=interactions.OptionType.STRING,
                 required=False
               )
            ]
        )       
    ]
)
async def khalti(ctx: interactions.CommandContext, sub_command:str = 'None', master_key: str = None, username:str = None,password:str = None, repeat_master_key:str = None, code:int = None,khalti_id:str = True, amount:int = None,purpose:str  = 'Personal Use', remarks:str = 'Transaction made through Routiney discord bot', number_to_topup:int = None,hide_message:bool=True):
    headers={'Deviceid':'khalti-discord-'+str(ctx.author.id)}
    headers['Content-Type']= 'application/json'
    # headers['Content-Type']= 'application/json;charset=UTF-8'
    global temp_otp_token
    if master_key or repeat_master_key:
        if repeat_master_key:
            master_key=repeat_master_key
        encryptionKey = master_key[:32].zfill(32).encode('ascii')
        cipher = AES.new(encryptionKey, AES.MODE_ECB)
        enc_userID = str(base64.b64encode(cipher.encrypt(pad(str(ctx.author.id).encode("ascii"), AES.block_size))))[2:-1]
        if not sub_command=='login':
            select_user=collection.find_one({ "userID": str(ctx.author.id)})
            if  select_user == None:
                await ctx.send("You are not logged in!", ephemeral=True)
                return
            elif select_user['enc_userID'] != str(enc_userID):
                if sub_command=='otp':
                    await ctx.send("Looks like you forgot your master key, Please login again", ephemeral=True)
                    temp_otp_token.pop(str(ctx.author.id))
                    collection.delete_one({"userID" : str(ctx.author.id)})
                else:
                    await ctx.send("Incorrect Master Key provided! You can re-login if you forgot your master key.", ephemeral=True)
                return
            else:
                if not sub_command=='otp':
                    dec_token = unpad(cipher.decrypt(base64.b64decode(select_user['enc_token'].encode())), AES.block_size).decode()
                    headers['Authorization']='Token '+dec_token
    if sub_command=='login':
        login_data={"password":password,"id":username}
        r=requests.post('https://khalti.com/api/auth/login-wallet/',headers=headers,data=login_data)
        if r.status_code==200:
            if not 'Please enter the code to continue' in r.text:
                await ctx.send('Logged in!', ephemeral=True)   
                return
            await ctx.send('Enter the OTP code', ephemeral=True)            
            collection.find_one_and_update({ "userID": str(ctx.author.id)},{ "$set": { "enc_userID": enc_userID} },upsert=True)
            r=r.json()
            temp_otp_token[str(ctx.author.id)]=[r["verification_data"]["idx"],r["verification_data"]["verification_token"]]
        else:
            await ctx.send(r.text, ephemeral=True)
    if sub_command=='otp':
        if not str(ctx.author.id) in temp_otp_token:
            await ctx.send("You have to login first before entering OTP", ephemeral=True)
            return        
        otp_data={"code":str(code),"verification_token":temp_otp_token[str(ctx.author.id)][1]}
        r=requests.post(f'https://khalti.com/api/v2/dkey/{temp_otp_token[str(ctx.author.id)][0]}/verify_web_otp/',headers=headers,data=otp_data)
        if r.status_code==200:
            r=r.json()
            await ctx.send(f"Logged in as **{r['name']}**", ephemeral=True)
            enc_token = str(base64.b64encode(cipher.encrypt(pad(r['token'].encode("ascii"), AES.block_size))))[2:-1]
            collection.find_one_and_update({ "userID": str(ctx.author.id)},{ "$set": { "enc_token": enc_token} },upsert=True)
        else:
            await ctx.send(r.text, ephemeral=True)
    if sub_command=='info':
        info_data={"my_info":{"url_name":"my-info"}}
        r=requests.post('https://khalti.com/api/data/refresh/', headers=headers,data=json.dumps(info_data))
        if r.status_code==200:
            r=r.json()
            embed = interactions.Embed(
                author=interactions.EmbedAuthor(name=f"{r['my_info']['data']['user']['name']}", icon_url=f"{r['my_info']['data']['user']['pp']}"),
                title="",
                description="",
                fields = [
                    interactions.EmbedField(name="Phone", value=f"{r['my_info']['data']['user']['mobile']}"),
                    interactions.EmbedField(name="Email", value=f"{r['my_info']['data']['user']['email']}"),
                    interactions.EmbedField(name="DOB", value=f"{r['my_info']['data']['user']['dob']}"),
                    interactions.EmbedField(name="Gender", value=f"{r['my_info']['data']['user']['gender']}"),
                    interactions.EmbedField(name="Referral URL", value=f"{r['my_info']['data']['user']['referral_url']}"),
                    interactions.EmbedField(name="Profile Status", value=f"{r['my_info']['data']['user']['profile_status']}")
                ],
                thumbnail=interactions.EmbedImageStruct(url=f"{r['my_info']['data']['user']['qrcode']}"),
                footer=interactions.EmbedFooter(text="Account Created On "),
                timestamp = r['my_info']['data']['user']['created_on']
            )
            await ctx.send(embeds=embed, ephemeral=True)
        else:
            await ctx.send(r.text, ephemeral=True)         
    if sub_command=='qr':
        info_data={"my_info":{"url_name":"my-info"}}
        r=requests.post('https://khalti.com/api/data/refresh/', headers=headers,data=json.dumps(info_data))
        if r.status_code==200:
            r=r.json()
            embed = interactions.Embed(
                description=f"Scan the QR to pay {r['my_info']['data']['user']['name']}",
                image =interactions.EmbedImageStruct(url=r['my_info']['data']['user']['qrcode'])
            )
            await ctx.send(embeds=embed, ephemeral=False)
        else:
            await ctx.send(r.text, ephemeral=True)         
    if sub_command=='balance':
        info_data={"my_info":{"url_name":"my-info"}}
        r=requests.post('https://khalti.com/api/data/refresh/', headers=headers,data=json.dumps(info_data))
        if r.status_code==200:
            r=r.json()
            tosend=f"You've got Rs. {str(round(int(r['my_info']['data']['balance']['primary'])/100, 1))} in your wallet."
            await ctx.send(tosend, ephemeral=hide_message)
        else:
            await ctx.send(r.text, ephemeral=True)         
    if sub_command=='history':
        d=datetime.timedelta(days = 28)
        tod = datetime.datetime.now()
        start = tod - d
        r=requests.get(f"https://khalti.com/api/transaction/?start_date={start.strftime('%Y-%m-%d')}&end_date={tod.strftime('%Y-%m-%d')}", headers=headers)
        if r.status_code==200:
            r=r.json()
            embed = interactions.Embed(
                description="Last 5 Transactions in last 28 days",
            )
            rec=r['records']
            for i in range(5):
                try:
                    parsedate=datetime.datetime.strptime(rec[i]['created_on'],'%Y-%m-%dT%H:%M:%S.%f%z')
                    val=''
                    for k in rec[i]['transaction_params'].keys():
                        val+=rec[i]['transaction_params'][k]+ ' | '
                    val+=rec[i]['state']['name']
                    embed.add_field(name=f"{rec[i]['title']} @ {parsedate.strftime('%d %h %H:%M')}: {'-' if rec[i]['balance']['type']=='debit' else '+'}{str(round(int(rec[i]['amount'])/100,1))}", value=val)
                except:
                    break
            await ctx.send(embeds=embed, ephemeral=hide_message)
        else:
            await ctx.send(r.text, ephemeral=True)      
    if sub_command=='topup':
        number_to_topup=str(number_to_topup)
        if len(number_to_topup) !=10:
            await ctx.send('Invalid mobile number!', ephemeral=True)
            return
        provider_id=int(number_to_topup[2:][0])    
        if provider_id in [0,1,2]: provider='ncell/'
        elif provider_id in [4,6]: provider='ntc/'
        elif provider_id == 8: provider='smartcell/'
        elif provider_id == 5: provider='nt-postpaid/'
        else: 
            await ctx.send('Provided number doesnt exist!', ephemeral=True)
            return
        topup_data={"number":number_to_topup,"amount":str(amount)}
        r=requests.post('https://khalti.com/api/v2/service/use/'+provider, headers=headers,data=json.dumps(topup_data))
        if r.status_code==200:
            r=r.json()
            tosend=f"Sucessfully recharged {number_to_topup} with Rs. {str(amount)}. "
            if hide_message:
                tosend+=f"Your balance is now Rs. {str(round(int(r['meta']['balance']['primary'])/100,1))}"
            await ctx.send(tosend, ephemeral=hide_message)
        else:
            await ctx.send(r.text, ephemeral=True)
    if sub_command=='transfer':
        transfer_data={"user":khalti_id,"amount":str(amount*10),"purpose":purpose,"remarks":remarks,"partial_payment":None}
        r=requests.post('https://khalti.com/api/v2/fund/v2/offer/', headers=headers,data=json.dumps(transfer_data))
        if r.status_code==200:
            r=r.json()
            tosend=f"Sucessfully sent Rs. {str(round(int(r['amount'])/100,1))} to {khalti_id}. "
            if hide_message:
                tosend+=f"Your balance is now Rs. {str(round(int(r['meta']['balance']['primary'])/100,1))}"
            await ctx.send(tosend, ephemeral=hide_message)
        else:
            await ctx.send(r.text, ephemeral=True)         
    if sub_command=='logout':
        if master_key:
            r=requests.post('https://khalti.com/api/auth/logout/', headers=headers)
        collection.delete_one({"userID" : str(ctx.author.id)})
        await ctx.send('Logged out!', ephemeral=True)
bot.start()
