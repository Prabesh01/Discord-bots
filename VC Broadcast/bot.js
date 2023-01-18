const { ActivityType, Client, EmbedBuilder,GatewayIntentBits  } = require('discord.js');
const { EndBehaviorType,joinVoiceChannel,VoiceConnection   } = require('@discordjs/voice');
const fs = require("fs");
const config = require("./config.json");
const { spawn } = require('child_process');
const { OpusDecoder } = require("audify");

var sth=Date.now();
const decoder = new OpusDecoder(48000, 2);

var child=''

child = spawn('ffmpeg',['-re','-loop', '1', '-framerate', '2', '-i', config.image,'-f', 's16le', '-ar', '48k', '-ac', '2', '-re', '-i', 'pipe:0', '-c:a', 'aac', '-s','1920x1080','-ab', '128k', '-b:v', '2500k', '-threads', '6', '-qscale', '3', '-preset', 'veryfast', '-vcodec', 'libx264', '-pix_fmt', 'yuv420p', '-maxrate', '2048k', '-bufsize', '2048k', '-framerate', '30', '-g', '2', '-strict', 'experimental','-f', 'flv', 'rtmp://a.rtmp.youtube.com/live2/'+config.yt_stream_key],{ stdio: ['pipe']
})

child.stdout.setEncoding('utf8');
child.stdout.on('data', function(data) {
    console.log('stdout: ' + data);
});
child.stderr.on('data', function(data) {
    console.log('stderr: ' + data);
});
child.on('close', function(data) {
    console.log('close: ' + data);
    child.stdin.end()
    child.kill()
child = spawn('ffmpeg',['-re','-loop', '1', '-framerate', '2', '-i', config.image,'-f', 's16le', '-ar', '48k', '-ac', '2', '-re', '-i', 'pipe:0', '-c:a', 'aac', '-s','1920x1080','-ab', '128k', '-b:v', '2500k', '-threads', '6', '-qscale', '3', '-preset', 'veryfast', '-vcodec', 'libx264', '-pix_fmt', 'yuv420p', '-maxrate', '2048k', '-bufsize', '2048k', '-framerate', '30', '-g', '2', '-strict', 'experimental','-f', 'flv', 'rtmp://a.rtmp.youtube.com/live2/'+config.yt_stream_key],{ stdio: ['pipe']
})
});

var killWorkers = function() {
    child.stdin.end()
    child.kill();
    process.exit(0);
};

process.on("uncaughtException", killWorkers);
process.on("SIGINT", killWorkers);
process.on("SIGTERM", killWorkers);

var emptychunk
fs.readFile('1.pcm', 'utf8', function(err, data){
        emptychunk=data
})

var stat='';

function delay(time) {
  return new Promise(resolve => setTimeout(resolve, time));
}

async function doSomething() {
        if((Date.now()-sth)/1000>=2){
                if(stat==null) return
                stat=null;
                while(stat==null){

                    child.stdin.write(emptychunk)
                        await delay(1000);
                }
        }
}

const client = new Client({
        intents: [
                GatewayIntentBits.Guilds,
                GatewayIntentBits.GuildMessages,
                GatewayIntentBits.MessageContent,
                GatewayIntentBits.GuildMembers,
                GatewayIntentBits.GuildVoiceStates,
        ],
});

var listener=function(text='listener hit') {
  console.log(text);
};


function safelyWriteDataToStdin(stdin, data) {
stdin.once("error", listener);
    stdin.write(
      data
    );
stdin.removeListener("error",listener);
}


client.on("ready", () => {
 setInterval(doSomething, 2000)
  console.log(`Bot has started, with ${client.users.cache.size} users, in ${client.channels.cache.size} channels of ${client.guilds.cache.size} guilds.`);
  client.user.setActivity('VC audio to YouTube',{type: ActivityType.Streaming, name:'YouTube', url: config.yt_livestream_url,});
});

client.on("messageCreate", async message => {
  if(message.author.bot) return;
  if(message.author.id!=config.ownerID) return;
  if(!message.content.startsWith(config.prefix)) return;

  const args = message.content.slice(config.prefix.length).trim().split(/ +/g);
  const command = args.shift().toLowerCase();

  if(command === "join") {
    if (!message.member.voice.channel) return message.reply('Please join a voice channel first!');
    if ((message.member.voice.channel.members.filter((e) => client.user.id === e.user.id).size > 0)) return message.reply(`I'm already in your voice channel!`);
    if(message.member.voice.channel.type == "GUILD_STAGE_VOICE"){}else{
    if (!message.member.voice.channel.joinable) return message.reply(`I don't have permission to join that voice channel!`);
}
const connection = joinVoiceChannel(
{
    channelId: message.member.voice.channel.id,
    guildId: message.guild.id,
    adapterCreator: message.guild.voiceAdapterCreator,
    selfDeaf: false,
});

    const receiver = connection.receiver;
var alrdy=null
    receiver.speaking.on("start", (userId) => {
if((Date.now()-sth)/1000>=2){
       sth=Date.now();
        alrdy=userId
}else{
        return
}
stat='12';
let subscription = receiver.subscribe(userId, { end: { behavior: EndBehaviorType.AfterSilence, duration: 1500}});

      subscription.on("data", chunk => {
sth=Date.now();
                  safelyWriteDataToStdin(child.stdin, decoder.decode(chunk, 960)) //.then((error)=>console.log("The error is:", error ));

});

    });
  }

  if(command === "fag") {
        try {
    await message.guild.members.me.voice.disconnect();
        }catch(err) {
                console.log(err)
        return;
        }
  }


});

client.login(config.token);
