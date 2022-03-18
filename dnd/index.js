const fs = require('node:fs');
const { Client, Collection, Intents } = require('discord.js');
const { token } = require('./config.json');
const { createLogger, format, transports } = require("winston");
 
const logger = createLogger({
  format: format.combine(format.timestamp(), format.json()),
  transports: [new transports.Console({})],
});
// const myIntents = new Intents();
// myIntents.add(Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_PRESENCES, Intents.FLAGS.GUILD_MEMBERS, Intents.FLAGS.GUILD_MESSAGES,Intents.FLAGS.DIRECT_MESSAGES);

const client = new Client({ intents: ["GUILDS","GUILD_PRESENCES", "GUILD_MEMBERS", "GUILD_MESSAGES", "DIRECT_MESSAGES"], partials: ['CHANNEL',]});

client.on('error', console.error); 

// const client = new Client({ intents: myIntents });

// const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

const eventFiles = fs.readdirSync('./events').filter(file => file.endsWith('.js'));

client.commands = new Collection();
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
	const command = require(`./commands/${file}`);
	client.commands.set(command.data.name, command);
}

for (const file of eventFiles) {
	const event = require(`./events/${file}`);
	const eventName = file.split(".")[0];
	const eventType = file.split(".")[1];
	if (eventType=='o') {
		//client.once(eventName, (...args) => event.execute(...args));
		client.once(eventName, event.bind(null, client));
	} else {
		//client.on(event.name, (...args) => event.execute(...args));
		client.on(eventName, event.bind(null, client));
	}
}


client.on('presenceUpdate', (oldPresence, newPresence) => {
    let member = newPresence.member;
	if(member.id in ursl){
	try{
	if(newPresence.status!='dnd'){
		delete ursl[member.id];
	}
	}catch(error) {
		console.error(error);
	}
	}
});


client.on('interactionCreate', async interaction => {
	if (!interaction.isCommand()) return;

	const command = client.commands.get(interaction.commandName);

	if (!command) return;

	try {
		await command.execute(interaction);
	} catch (error) {
		console.error(error);
		await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
	}
});

client.login(token);



// client.on('interactionCreate', async interaction => {
	// if (!interaction.isCommand()) return;
	
// // 	const command = client.commands.get(interaction.commandName); // //
// // if (!command) return; // //
// // 		await command.execute(interaction); // //


	// const { commandName } = interaction;

	// if (commandName === 'ping') {
	//	try {
		// await interaction.reply('Pong!');
	// } catch (error) {
		// console.error(error);
		// await interaction.reply({ content: 'Sth went wrong ;/', ephemeral: true });
	// } else if (commandName === 'server') {
		// await interaction.reply(`Server name: ${interaction.guild.name}\nTotal members: ${interaction.guild.memberCount}`);
	// } else if (commandName === 'user') {
		// await interaction.reply(`Your tag: ${interaction.user.tag}\nYour id: ${interaction.user.id}`);
	// }
// });
