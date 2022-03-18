const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('clear')
		.setDescription('Clear DND status of a member')
		.addUserOption(option=> option.setName("select").setDescription("Select a user").setRequired(true)),
	async execute(interaction) {
		if (!(interaction.member.permissions.has("MODERATE_MEMBERS"))){
			await interaction.reply({content: "Only server moderators can use this command!", ephemeral: true});
			return;
		}
		const target=interaction.options.getUser("select");
		if (target.bot){
			await interaction.reply({content: "That's a bot", ephemeral: true});
			return
		}
		if (target.id in ursl){
			delete ursl[target.id];
			await interaction.reply(`Cleared DND of <@${target.id}>`);
		}else{
			await interaction.reply({content: "This user has not set any DND status", ephemeral: true});
		}
		return
	},
};