## Bot Info

- Official Website: [ronb.xyz](https://ronb.xyz)
- Top.gg Link: https://top.gg/bot/786534057437691914#/
- [Bot Invite Link](https://discord.com/api/oauth2/authorize?client_id=786534057437691914&permissions=536963136&scope=bot) • [Support Server](https://discord.gg/ehRSPHuTDy)

## Configuration

**Here's a quick video for those who didn't understand the instructions below:** https://www.youtube.com/watch?v=dQw4w9WgXcQ

_Simply [download this directory](https://downgit.github.io/#/home?url=https://github.com/Prabesh01/Discord-bots/tree/main/Routiney) then provide some values and the bot is ready. Easy as pie!_

1) Make sure you have all the required python modules installed:
      - Simply, run the command ```pip install -r requirements.txt``` to do so
 
2) Provide the required values in bot.py as mentioned:
      - In line 30, put bot's token value in DISCORD_TOKEN
      - line 31, log, put discord webhook URL of a channel where the bot will posts about the errors it faced
      - For line 34-37, run the script [step3.py](https://github.com/Prabesh01/Discord-bots/blob/main/Routiney/step3.py). It will tell you what to keep in which line.

3) You have to provide your facebook cookies to the script to avoid getting blocked by facebook. The script will then scrape page as a user account.
  
    To do so, temporarily install a cookie editor browser extention for [chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=en) or [firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/). Then go to facebook.com and open the addon from browser's menubar. Then copy the cookie using the export button present at bottom right.
  
    Now visit [this site](http://www.linuxonly.nl/docs/60/159_Convert_cookies_txt_format.html) to convert the copied cookie to understandable form by the script. After converting, keep it in a file named cook.txt in the same directory as of bot.py
      - Make sure to leave a empty line at the end of cook.py i.e. the last line of cook.py must be blank.
      - If you logout from facebook in the browser, the cookie will be invalid so you need to repeat this step to get new working cookie.

## This is it! 
   now run the bot.py python script and the bot will start sending RONB fb posts once you subscribed a channel using command r!sub and also enjoy oa command. xD

## Self-hosting

Bot's code provided here is primarily for the transparency reasons and to help other developers implement the same functionality to their bots.

Given the bot's simple nature, using the publicly-hosted version will be enough for most people, so it is highly recommended to use that version, unless you have a specific reason not to do so (such as experimenting with the code).

You're free to host this bot on your own server (if you get above instructions to set it up), however I will not be providing any support in that regard, do it at your own risk. Please keep in mind that if you're directly hosting this bot, you might not monetize it in any way!
