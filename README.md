### __routiney.py + hook.py + .env__

- routiney.py: Keeps the bot online 24/7, replies to pre-defined commands, subscribes and unsubscribe channels. Preferred to keep this script running in background.
- hook.py: scrape latest posts from the page and send to the wehooks collected by routiney.py. Preferred to keep this script in cron job to run in every x minutes.
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
- Create a bot from [here](https://discord.com/developers/applications/) and invite it to your server with administrative permission 
- Replace bot token in .env file
- To serve the bot, keep routiney.py running in backgroung using<br>
```nohup python3 routiney.py &``` <br>
and keep hook.py in cronjob (crontab -e) as: <br>
```* * * * * python3 hook.py```

_I would suggest to keep all files in home directory rather than other because when a script is running through crontab, it runs from home directory; means all its output file would be in home directory and required files should be in home directory for it to fuction without any problem. If you added the script to crontab with root accout, the script will run from /root directory._
