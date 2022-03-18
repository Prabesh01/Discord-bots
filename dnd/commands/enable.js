const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('enable')
		.setDescription('Enable DND bot')
		.addSubcommand(subcommand=>
			subcommand
				.setName("server")
				.setDescription("Enable all disabled channels")
			)
		.addSubcommand(subcommand=>
			subcommand
				.setName("channel")
				.setDescription("Enable a disabled channel")
				.addChannelOption(option=> option.setName("select").setDescription("Select a channel").setRequired(true)))
		.addSubcommand(subcommand=>
			subcommand
				.setName("member")
				.setDescription("Unban a banned user")
				.addUserOption(option=> option.setName("select").setDescription("Select a user").setRequired(true))),
	async execute(interaction) {
		if (!(interaction.member.permissions.has("ADMINISTRATOR"))){
			await interaction.reply({content: "Only server admins can use this command!", ephemeral: true});
			return;
		}
		const selected=interaction.options.getSubcommand();
		const guild=interaction.guild
		const user=interaction.user
		
		if(selected=='server'){
			is=0
			console.log(shlz)
			if (guild.id in shlz){
				delete shlz[guild.id];
				is=1
			}
			if (guild.id in chlz){
				delete chlz[guild.id]
				is=1
			}
			if(is==0){
				await interaction.reply({content: "Any Channel of this server isn't disabled.", ephemeral: true});
			}else{
				await interaction.reply('👌‌');
			}
		}else if (selected=='channel'){
			console.log(chlz)
			const channel=interaction.options.getChannel("select");
			if(channel.type!="GUILD_TEXT"){
				await interaction.reply({content: "Select a text channel!", ephemeral: true});
				return
			}
			if (guild.id in shlz){
				if (shlz[guild.id].includes(channel.id)){
					await interaction.reply({content: `<#${channel.id}> was already enabled`, ephemeral: true});
					return
				}else{
					shlz[guild.id].push(channel.id)
					await interaction.reply(`Enabled <#${channel.id}>`);
                                        return
				}
			}
			if (guild.id in chlz){
				if (chlz[guild.id].includes(channel.id)){
					for( var i = 0; i < chlz[guild.id].length; i++){ 
						if ( chlz[guild.id][i] === channel.id) { 
							chlz[guild.id].splice(i, 1); 
						break
						}
					}
					await interaction.reply(`Enabled <#${channel.id}> sucessfully.`);
					return
				}else{
					await interaction.reply({content: `<#${channel.id}> was never disabled`, ephemeral: true});
					return
				}
			}
			await interaction.reply('👌‌');
			return
		}else{			
			console.log(mhlz);
			const target=interaction.options.getUser("select");
			if (target.bot){
				await interaction.reply({content: "That's a bot", ephemeral: true});
				return
			}
			if (guild.id in mhlz){
				if (mhlz[guild.id].includes(target.id )){
					for( var i = 0; i < mhlz[guild.id].length; i++){ 
						if ( mhlz[guild.id][i] === target.id) { 
							mhlz[guild.id].splice(i, 1); 
						break
						}
					}
					await interaction.reply(`<@${target.id}> can now use the bot in this server`);
					return
				}
			}
			await interaction.reply({content: `<@${target.id}> wasn't banned`, ephemeral: true});
			return;
		}
		return;
	},
};
