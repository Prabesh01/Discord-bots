// module.exports = {
// name: 'guildCreate',
// execute(client, guild) {  
  // console.log(`[GUILD JOIN] ${guild.id} added the bot. Owner: ${guild.ownerId}`)
  // },
// 
const { WebhookClient } = require('discord.js');
module.exports = (client, guild) => {
  msg=`[DND JOIN] ${guild.id} - ${guild.name}`;
const webhook = new WebhookClient({ url: 'https://discord.com/api/webhooks/823071522582560818/EPUgMR0KlZEVjpsIEanc6Kc6fT8B2nRIDUMwuSYMnvLAsYU1ttGgwQM2Qre5pqO6cW93' });
webhook.send(msg)
};
