# Content
- [Scrape fb page and send discord message for every new post by a page](#routiney)
- [Send discord message for every new youtube notification](#youtubey)
- [Send discord message for every new facebook message](#hulaki)
- [Get discord channel message for new gmail mails](#zapier)
- [Get discord channel message for new tweets by selected public page](#tweetshift)
- [Role reward bot based on mee6 level](#role_reward)
- [Fetch particular content from image (news paper in this case) and post it to discord](#abin)

_In the script, text files are used to store and process channel IDs and URLs to use as less resource as possible because I was using free tier of EC2 instance of AWS. It is strongly recommended to store and process these data using some database managers like panda or something else_

# <a name="routiney"></a> 
## __routiney.py + hook.py + .env__ (Scrape fb page and send discord message for every new post by a page)

- routiney.py: Keeps the bot online 24/7, replies to pre-defined commands, subscribes and unsubscribe channels. Preferred to keep this script running in background.
- hook.py: scrape latest posts from the facebook page and send to the wehooks collected by routiney.py. Preferred to keep this script in cron job to run in every x minutes.
- .env: just for bot authorization

##### Usage
- Invite the bot to your server (guild) from [here](https://discord.com/api/oauth2/authorize?client_id=786534057437691914&permissions=8&scope=bot)
- Enter `r!` in any text channel to check if the bot has entered your server sucessfully
- Enter `r!sub` in a text channel where you want to receive lastest RONB posts
- Use `r!unsub` to unsubscribe

##### Bot Setup (only for developers, not for normal bot users):

###### Dependencies
```pip install discord.py```<br>
```pip install discord_webhook```<br>
```pip install -U python-dotenv``` <br>
```pip install facebook_scraper```<br>

###### Steps
- Create a bot from [here](https://discord.com/developers/applications/) and invite it to your server with minimum permission of 536889344
- Replace bot token in .env file
- To serve the bot, keep routiney.py running in backgroung using<br>
```nohup python3 routiney.py &``` <br>
and keep hook.py in cronjob (crontab -e) as: <br>
```* * * * * python3 hook.py```

_I would suggest to keep all files in home directory rather than other because when a script is running through crontab, it runs from home directory; means all its output file would be in home directory and required files should be in home directory for it to fuction without any problem. If you added the script to crontab with root accout, the script will run from /root directory._

# <a name="youtubey"></a> 
## __youtubey.py__ (Send discord message for every new youtube notification)

##### Usage
 - Note down the webhook url of the channel you want the notification to be sent. Then Go to youtube.com. After it loads, open network tab in developers tool and click on notification icon in youtube homepage. In network tab, search for 'get_notification_menu'. You will probably see one request. See request header (enable raw view for ease) and note down these 5 values: 
    - Api Key (POST /youtubei/v1/notification/get_notification_menu?key=XXXXXXXX)
    - User Agent (User-Agent: XXXXXXX)
    - Authorization Header (Authorization: XXXXXXXX)
    - __Secure-3PSID Value (Cookie)
    - __Secure-3PAPISID Value (Cookie)
- Enter above 6 values including webhook url in youtubey.py from line 10-15 in respective places.
- Finally, keep youtubey.py in cronjob (crontab -e) as: <br>
```0 * * * * python3 youtubey.py```<br>
This will check notification every hour and send discord messages if new notificaton is detected.

# <a name="hulaki"></a> 
## __hulaki.py__ (Send discord message for every new facebook message)

##### Usage
 - Note down the webhook url of the channel you want the notification to be sent. Then copy xs and c_user value from cookie of facebook.com or m.facebook.com or mbasic.facebook.com.
 -  Enter above 3 values including webhook url in youtubey.py from line 8-11 in respective places. Enter Useragent too if you faced some problems.
- Finally, keep youtubey.py in cronjob (crontab -e) as: <br>
```0 * * * * python3 hulaki.py```<br>
This will check new messages every hour and send discord messages if new message is detected.

# <a name="zapier"></a> 
## __zapier.com__ (Get discord channel message for new gmail mails)

##### Usage:
- Just setup these two zaps and you are done:
 - [Add rows to Google Sheets with new emails on Gmail](https://zapier.com/app/editor/114807052/nodes/114807052/auth)
 - [Send Discord channel messages with new Google Sheets rows](https://zapier.com/app/editor/114807030/nodes/114807030/auth) <br>
Direct integration between discord and gmail used to be available but recently after few changes in google's privacy policy it is no longer supporter. That's why we have to use google sheet as bridge between discord and gmail. Alternatively, you can use automate.io.

# <a name="tweetshift"></a>
## tweetshift (Get discord channel message for new tweets by selected public page)

##### Usage:
- Just invite [this bot](https://discord.com/oauth2/authorize?client_id=713026372142104687&permissions=537160768&redirect_uri=https://tweetshift.com/invite/callback&response_type=code&scope=bot) and you are done. Type t!help in server after inviting bot to know about commands and set it up easily.

# <a name="role_reward"></a>
## mee6.py (Give roles to server members based on mee6 level)

##### Info:
- Mee6 discord bot has some features limited to premium members. Those features are cool but isn't quite important to have in normal servres so mee6 free membership is just fine. But one important feature that is not available for mee6 free users is the level based rewards. 
- Using this mee6.py, your bot in the server will fetch your server's leaderboard from [mee6 api](https://mee6.xyz/api/plugins/levels/leaderboard/server_id_here) and check each members level and gives roles as configured in the script.

##### Usage:
- Make sure mee6 leveling is enabled and your server's leaderboard is public.
- Have your bot that will give the roles to your server members, ready in the server with all required permissions to the bot.
- Provide the required values in mee6.py from line 5-11
- Run the script in cronjob for every one day or one hour based on how busy your server is. Or you can remove the sys.exit() in line 51 and run the on_ready fuction in loop every one hour or so using tasks.loop.

# <a name="abin"></a>
## abin.py (Fetch particular content from image and post it to discord)

##### Usage:
- Just install the imported libraries, provide your webhook url or list of webhooks in line 25,download the given template imag (ab.png) and run the script everyday after 10am.
