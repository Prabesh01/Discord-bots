# Ignore this directory. These are the scripts I tried, which somehow works but is all messed up and isn't trustworthy.
_You can use these codes as reference on how not to code a discord bot_

# routiney.py + env

#### Usage
- Invite the bot to your server (guild) from [here](https://discord.com/api/oauth2/authorize?client_id=786534057437691914&permissions=8&scope=bot)
- Enter `r!` in any text channel to check if the bot has entered your server sucessfully
- Enter `r!sub` in a text channel where you want to receive lastest RONB posts
- Use `r!unsub` to unsubscribe

#### Bot Setup (only for developers, not for normal bot users):

###### Dependencies
```pip install discord.py```<br>
```pip install discord_webhook```<br>
```pip install -U python-dotenv``` <br>
```pip install facebook_scraper```<br>

###### Steps
- Replace bot token in .env file
- To serve the bot, keep the script in cronjob (crontab -e) as: <br>
```* * * * * timeout 58 python3 routiney.py```


# final.py
I won't even bother to tell about this shit.

```Legends don't look back at the mess they have created```
