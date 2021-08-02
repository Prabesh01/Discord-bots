## Configuration

_You can simple copy paste the code as it is and provide some values and the bot is ready. If you feel setting up tiresome, remember that this is one time setup. Once you configured the script, you can just let the script run and you have to do nothing_

1) There's a code in the script for posting server count to top.gg. So if you are using the bot for personal use and dont have your bot in top.gg or don't wan't to post, you have to remove these lines:
      - 14, 38, 40, 43-47 and 159-60
      - But removing these line will change the page's line count and will conflict with line number I will be mentioning below so remove these lines at last

2) Make sure you have all the required python modules installed:
      - discord.py, discord-webhook, discord-together, topggpy, discord-ext-bot, facebook-scraper, discord-webhook, langdetect, nepali-datetime
 
3) Provide the required value to variables as mentioned:
  - In line 30, put bot's token value in DISCORD_TOKEN
  - line 31, log, put discord webhook URL of a channel where the bot will posts about the error it faced
  - For line 34-37, .............. (will complete this point later)

4) Scrapping facebook is pain in ass 'cause facebook tries its best to block automation scripts. Using the script for long time might result in ban to you IP for 1 hour or so. This can't be helped but can be minimized using cookies. Provide your facebook cookies to the script and it will scrape page as a user account.
  
    To do so, temporarily install a cookie editor browser extention for [chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=en) or [firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/). Then go to facebook.com and open the addon from browser's menubar where addons are. Then copy the cookie using the export button present at bottom right.
  
    Now visit [this site](http://www.linuxonly.nl/docs/60/159_Convert_cookies_txt_format.html) to convert the copied cookie to understandable form by the script. After converting, keep it in a file named cook.txt in the same directory as of bot.py
      - If you logout from facebook in the browser, the cookie will be invalid so you need to repeat this step to get new working cookie.

## This is it! 
   now run the python script and the bot will start sending RONB fb posts once you subsribed a channel using command r!sub and also enjoy oa command and repost feature.
