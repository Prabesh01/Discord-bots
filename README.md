#### routiney.py

##### Usage
- Invite the bot to your server (guild) from [here](https://discord.com/api/oauth2/authorize?client_id=786534057437691914&permissions=8&scope=bot)
- Enter `r!` in any text channel to check if the bot has entered your server sucessfully
- Enter `r!sub` in a text channel where you want to receive lastest RONB posts
- Use `r!unsub` to unsubscribe

##### Bot Setup (only for developers, not for normal bot users):

###### Dependencies
```pip install discord.py```<br>
```pip install -U python-dotenv``` <br>
```pip install facebook_scraper```<br>

###### Steps
- Create a bot from [here](https://discord.com/developers/applications/) and invite it to your server with administrative permission 
- Replace bot token in .env file
- To serve the bot, keep routiney.py running in backgroung using<br>
```nohup python3 routiey.py &``` <br>
and keep hook.py in cronjob (crontab -e) as: <br>
```* * * * * python3 hook.py```

_I would suggest to keep all files in home direstory rather than other 'cause when a script is running through crontab, it runs from home directory; means all its required files and output file should be in home directory for it to fuction without any problem. If you added the script to crontab with root accout, the script will run from /root directory._
