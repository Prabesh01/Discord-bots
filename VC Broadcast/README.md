## Self Hosting
- Make sure to enable all precenses for the bot from discord's developer portal.
- Make sure latest versions of node, ffmpeg along with all the required modules are installed.
- Enter required data in config.json. Get bot's token from https://discord.com/developers/applications and yt_stream_key from https://studio.youtube.com/channel/UC/livestreaming
- Then hit `nohup node bot.js &`
- Bot should be up. The only person whose userID is mentioned in `config.json` can use the command. Use "!join" to make bot join the VC and "!fag" to leave the VC
- Manage your livestream from https://studio.youtube.com/channel/UC/livestreaming/manage

### Points to know
 - Bot only listens to one user at a time no matter how many are speaking (The first user who speaks is listened to). If the currently listening user stops, another user is listened to.
 - Instead of directly streaming from https://studio.youtube.com/channel/UC/livestreaming, schedule a livestream from https://studio.youtube.com/channel/UC/livestreaming/manage. This way, the stream wont immediately close event if nothing is sent to youtube for a while. So you can restart the bot if livestream is interrupted for some reason and resume the last livestream. 

### Known Issues:
 - Sometimes, For some reason, the ffmpeg stops randomly with error code 255. Listener on Line 23 of bot.js makes sure to respawn the ffmpeg if it closes but it doesn't seem to be working. So nothing is broadcasted. Have to restart the bot in this case.
