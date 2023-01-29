var Discord  = require('discord.js');
var Imap     = require('imap'),
    inspect  = require('util').inspect;
const fs = require('fs');

var imap = new Imap({
    user: "XXXXXXXXXXX@gmail.com",
    password: "app-password-here", // create app password for your mail account from https://support.google.com/mail/answer/185833?hl=en
    host: "imap.gmail.com",
    port: "993",
    tls: "true",
        tlsOptions: { rejectUnauthorized: false }
});

const webhook = new Discord.WebhookClient({ url: 'https://discord.com/api/webhooks/XXXXXXXXXXXXXX/XXXXXXXXXXXXXXXX-XXXX-XXXXXXXXXXXXXXXXXXXXXX-XXXXX-XXXXXXXX' });

var lastlastone=[]
fs.readFile('mail.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  lastlastone=data.trim().split(",");
});

// const allIntents = new Discord.Intents(32767);

// const bot = new Discord.Client({intents: 32767})

// const bot = new Discord.Client({
        // intents: ["GUILDS", "GUILD_VOICE_STATES", "GUILD_MEMBERS", "GUILD_BANS", "GUILD_MESSAGES", "DIRECT_MESSAGES"]
// });

// bot.login(config.token);

function openInbox(callback) {
    imap.openBox('INBOX', true, callback);
}
var lastone=[];
// Send the newest message to discord
function sendNewest() {
    openInbox(function(err, box) {
        if (err) throw err;
                // console.log(box.messages.total + ':*')
        var f = imap.seq.fetch(box.messages.total + ':*', {
            bodies: ['HEADER.FIELDS (FROM TO SUBJECT)', '1'],
            struct: true
        })
        f.on('message', (message, index) => {
            message.on('body', (stream, info) => {
                var buffer = '', count = 0;
                var prefix = '(#' + index + ') ';

                stream.on('data', function(chunk) {
                    count += chunk.length;
                    buffer += chunk.toString('utf8');
                    // console.log(prefix + 'Body [%s] (%d/%d)', inspect(info.which), count, info.size);
                });

                stream.once('end', function() {
if(!(lastone.includes(buffer.length))){
if(!(lastlastone.includes(buffer.length.toString()))){
console.log(buffer.length)
                                        if(buffer.length<=300){
                                        webhook.send(buffer)
                                          .catch();
                    // var channel = bot.channels.get(config.channel); // announcments channel
                    // channel.send(buffer);
                                        webhook.send("https://cdn.discordapp.com/attachments/951810185205280781/954623686839775272/4M7IWwP.gif")
                                          .catch();

                    // console.log(prefix + 'Body [%s] Finished', inspect(info.which));
                }                       }
lastone.push(buffer.length);
fs.writeFile('mail.txt', lastone.toString(), err => {
  if (err) {
    console.error(err);
  }
});

}

                });

            });
        });

        f.once('error', function(err) {
            console.log('Fetch error: ' + err);
        });
        f.once('end', function() {
            console.log('Done fetching all messages!');
            // imap.end();
        });
    });

}

imap.on('end', function() {
console.log("here");
imap.on('mail', mail => {
        sendNewest();
    });
//sendNewest();
});

imap.once('error', function(err) {
        console.log("err here");
  console.log(err);
});

imap.once('end', function() {
  console.log('Connection endingg');
imap.on('mail', mail => {
        sendNewest();
    });
});

imap.once('ready', function() {
    imap.on('mail', mail => {
        sendNewest();
    });
    //imap.start()
    sendNewest();
});

imap.connect();
