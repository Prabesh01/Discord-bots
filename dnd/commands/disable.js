const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('disable')
		.setDescription('Disable DND bot')
		.addSubcommand(subcommand=>
			subcommand
				.setName("server")
				.setDescription("Disable dnd bot in whole server")
				.addChannelOption(option=> option.setName("except").setDescription("Exception: Allow the bot in a channel")))
		.addSubcommand(subcommand=>
			subcommand
				.setName("channel")
				.setDescription("Disable DND bot in a channel")
				.addChannelOption(option=> option.setName("select").setDescription("Select a channel").setRequired(true)))
		.addSubcommand(subcommand=>
			subcommand
				.setName("member")
				.setDescription("Ban a member from using DND bot in this server")
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
			console.log(shlz)
			const channel=interaction.options.getChannel("except");
			if (channel!=null){
				if(channel.type!="GUILD_TEXT"){
					await interaction.reply({content: "Select a text channel!", ephemeral: true});
					return
				}
			}
			if (guild.id in shlz){
				if (channel==null){
					if(shlz[guild.id]=== undefined || shlz[guild.id].length ==0){
						await interaction.reply({content: "DND was already disabled in this server", ephemeral: true});
						return
					}else{
						const lisy = shlz[guild.id].map(e => "<#" + e+"> ");
						await interaction.reply(`DND was already disabled in this server. Removed the existing exception of ${lisy}`);
						shlz[guild.id]=[];
						return
					}
				}else{
					if (shlz[guild.id]==channel.id){
						await interaction.reply({content: `DND was already disabled in this server with exception of <#${channel.id}>`, ephemeral: true});
						return;
					}else{
						if(shlz[guild.id].length==0){
							shlz[guild.id].push(channel.id);
							await interaction.reply(`DND was already disabled in this server. Added an exception for <#${channel.id}>`);
							return
						}else{
							const lisu = shlz[guild.id].map(e => "<#" + e+"> ");
							await interaction.reply(`DND was already disabled in this server. Removed the existing exception of ${lisu} and added new exception of <#${channel.id}>`);
							shlz[guild.id]=[];
							shlz[guild.id].push(channel.id)
							return
						}
					}
				}
			}else{
				if (guild.id in chlz){
					delete chlz[guild.id];
				}
				shlz[guild.id]=[]
				if (channel==null){
					await interaction.reply("DND has been disabled in this server");
					return
				}else{
					shlz[guild.id].push(channel.id)
					await interaction.reply(`DND has been disabled in this server with exception of <#${channel.id}>`);
					return
				}
			return
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
					for( var i = 0; i < shlz[guild.id].length; i++){ 
						if ( shlz[guild.id][i] === channel.id) { 
							shlz[guild.id].splice(i, 1); 
						break
						}
					}
					await interaction.reply(`<#${channel.id}> has been disabled`);
					return
				}else{
					await interaction.reply({content: `<#${channel.id}> was already disabled`,ephemeral: true });
					return
				}
			}
			if (guild.id in chlz){
				if (chlz[guild.id].includes(channel.id)){
					await interaction.reply({content: `<#${channel.id}> was already disabled`, ephemeral: true});
					return
				}else{
					chlz[guild.id].push(channel.id);
				}
			}else{
				chlz[guild.id]=[]
				chlz[guild.id].push(channel.id)				
			}
			await interaction.reply(`<#${channel.id}> has been disabled`);
			return
		}else{			
			console.log(selected);
			console.log(mhlz);
			const target=interaction.options.getUser("select");
			if (target.bot){
				await interaction.reply({content: "That's a bot", ephemeral: true});
				return
			}
			if (guild.id in mhlz){
				if (mhlz[guild.id].includes(target.id )){
					await interaction.reply({content: "This user was already banned from using the bot in this server.", ephemeral: true});
					return
				}else{
					mhlz[guild.id].push(target.id);
				}
			}else{
				mhlz[guild.id]=[];
				mhlz[guild.id].push(target.id);
			}
			await interaction.reply(`<@${target.id}> has been banned from using DND in this server`);
			return
		}
		return
	},
};
