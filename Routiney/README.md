**Here's a quick video for those who didn't understand the instructions below:** https://www.youtube.com/watch?v=dQw4w9WgXcQ

## Configuration

_Simply copy paste the code as it is then provide some values and the bot is ready. Easy as pie!_

1) Make sure you have all the required python modules installed:
      - Simply, run the command ```pip install -r requirements.txt``` to do so
 
2) Provide the required values as mentioned:
      - In line 30, put bot's token value in DISCORD_TOKEN
      - line 31, log, put discord webhook URL of a channel where the bot will posts about the errors it faced
      - For line 34-37, run the script [step3.py](https://github.com/Prabesh01/Discord-bots/blob/main/Routiney/step3.py). It will tell you what to keep in which line.

3) You have to provide your facebook cookies to the script to avoid getting blocked by facebok. The script will then scrape page as a user account.
  
    To do so, temporarily install a cookie editor browser extention for [chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=en) or [firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/). Then go to facebook.com and open the addon from browser's menubar. Then copy the cookie using the export button present at bottom right.
  
    Now visit [this site](http://www.linuxonly.nl/docs/60/159_Convert_cookies_txt_format.html) to convert the copied cookie to understandable form by the script. After converting, keep it in a file named cook.txt in the same directory as of bot.py
      - Make sure there is a blank line at the end in cook.txt
      - If you logout from facebook in the browser, the cookie will be invalid so you need to repeat this step to get new working cookie.

## This is it! 
   now run the python script and the bot will start sending RONB fb posts once you subsribed a channel using command r!sub and also enjoy oa command. xD
