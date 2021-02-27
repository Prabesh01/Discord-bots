_In the script, text files are used to store and process channel IDs and URLs to use as less resource as possible because I was using free tier of EC2 instance of AWS. It is strongly recommended to store and process these data using some database managers like panda or something else_

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

## __hulaki.py__ (Send discord message for every new facebook message)

##### Usage
 - Note down the webhook url of the channel you want the notification to be sent. Then copy xs and c_user value from cookie of facebook.com or m.facebook.com or mbasic.facebook.com.
 -  Enter above 3 values including webhook url in youtubey.py from line 8-11 in respective places. Enter Useragent too if you faced some problems.
- Finally, keep youtubey.py in cronjob (crontab -e) as: <br>
```0 * * * * python3 hulaki.py```<br>
This will check new messages every hour and send discord messages if new message is detected.

## __zapier.com__ (Get discord channel message for new gmail mails)

##### Usage:
- Just setup these two zaps and you are done:
 - [Add rows to Google Sheets with new emails on Gmail](https://zapier.com/app/editor/114807052/nodes/114807052/auth)
 - [Send Discord channel messages with new Google Sheets rows](https://zapier.com/app/editor/114807030/nodes/114807030/auth) <br>
Direct integration between discord and gmail used to be available but recently after few changes in google's privacy policy it is no longer supporter. That's why we have to use google sheet as bridge between discord and gmail.
