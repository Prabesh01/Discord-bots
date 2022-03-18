// module.exports = {
	// name: 'guildDelete',
	// execute(client, guild) {  
  // console.log(`[GUILD LEAVE] ${guild.id} removed the bot.`);
// },
// };
const { WebhookClient } = require('discord.js');
module.exports = (client, guild) => {
  if (!guild.available) return; // If there is an outage, return.
  msg=`[GUILD LEAVE] ${guild.id} removed the bot.`;
  msg=`[DND LEAVE] ${guild.id} - ${guild.name}`;
const webhook = new WebhookClient({ url: 'https://discord.com/api/webhooks/823071522582560818/EPUgMR0KlZEVjpsIEanc6Kc6fT8B2nRIDUMwuSYMnvLAsYU1ttGgwQM2Qre5pqO6cW93' });
webhook.send(msg)
};
