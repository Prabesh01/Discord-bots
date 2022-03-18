// module.exports = {
	// name: 'messageCreate',
	// execute(client, message) {
		// console.log(`${message.content}`);
	// },
// };
res=[
"Ayo why ping?",
"Cut the crap kid you're crossing the limit",
"Can't u just die?",
"Damn you're annoying",
"Stfu!!!! You dickhead",
"Bruhh stop itt or you'll be clapped",
"Yo yo yo hey hey hey stop!",
"Damn why are you like this!!!!!",
"Stop it or your career will be destroyed",
"Shoot up you fat piece of bacon",
"Yoo what do u think you're doing",
"Duck you Bruh",
"Do u wanna get a bullet on your butt",
"I'll put a beer bottle in your butt and burst it",
"-___—", "Damn bro you're annoying",
"Let me breathe",
"I hate you and your whole career",
"Your wife is in my bed bitch",
"Cut the shit you limp dick",
"Can u stop, just stop, just stoppppp, uhh f u",
"OK I'm really getting mad now stop or die",
"I'll surely block u",
"Don't ping me u pig",
"Ya ya u are a dick head",
"Tryna get attention puff fuck off",
"You're not funny kiddo",
"Come on ping once more and you're done",
"Abcdefu",
"what you gon do bitch",
"yeah fuck off stupid lame ass shit",
"clappin yo mama",
"i'll put my 8 inch fatneek in yo mama and bust her",
"yo mama gets clapped by horses",
"you fucked your career cause you couldn't fuck anything else",
"YOUR MOM'S A HOE",
"Lame"
]

module.exports = async (client, message) => {
	//
	if(message.author.bot) return;
	if(message.guild === null ){
		attachment_url = []
		if(message.attachments.size>0){
			console.log(message.attachments.size)
			message.attachments.forEach(Attachment => {
			attachment_url.push(Attachment.url);
        })
		if (message.content==""){
		client.channels.fetch('888624067656187924')
		 .then(channel => channel.send(`${message.author.tag} sent: \n\`\`\`${attachment_url.toString()}\`\`\``));
			
		}else{
		client.channels.fetch('888624067656187924')
		 .then(channel => channel.send(`${message.author.tag} sent: \n\`\`\`${message.content}\`\`\`\n\`\`\`${attachment_url.toString()}\`\`\``));
		}
		}else{
		client.channels.fetch('888624067656187924')
		 .then(channel => channel.send(`${message.author.tag} sent: \n\`\`\`${message.content}\`\`\``));
		}
		await message.channel.send(res[Math.floor(Math.random()*res.length)]);
		return
	}
	if (message.guild.id in shlz){
		if (shlz[message.guild.id].includes(message.channel.id)){
		}else{
			return
		}
	}
	if (message.guild.id in chlz){
		if(chlz[message.guild.id].includes(message.channel.id)){
			return
		}
	}
	if (message.guild.id in mhlz){
		if(mhlz[message.guild.id].includes(message.author.id)){
			return
		}		
	}
	
	if(message.author.id in ursl){
		delete ursl[message.author.id];
		await message.channel.send(`Welcome back <@${message.author.id}>! I've removed your DND.`).then(msg => {setTimeout(() => msg.delete(), 5000)});
		return
	}
	
	if (message.content=='.dnd' || message.content=='.Dnd' || message.content=='.DND'){
		const user = await message.guild.members.cache.get(message.author.id)
		if(user.presence.status!="dnd"){
			await message.react("❌");
			await message.channel.send(`You need to set your status from ${user.presence.status} to DND in order to use this command`).then(msg => {setTimeout(() => msg.delete(), 5000)});
			return
		}
		ursl[message.author.id]='defxt360!bo';
		await message.react("<a:tick:934091250213212170>");
		return
	}
	
	if(message.content.startsWith('.dnd ') || message.content.startsWith('.Dnd ') || message.content.startsWith('.DND ')) {
		reaz=message.content.slice(5);
		if(reaz.length>=50){
			await message.channel.send("Why don't you try something short. Like your weenie");
			return
		}
		const user = await message.guild.members.cache.get(message.author.id)
		if(user.presence.status!="dnd"){
			await message.react("❌");
			await message.channel.send(`You need to set your status from ${user.presence.status} to DND in order to use this command`).then(msg => {setTimeout(() => msg.delete(), 5000)});
			return
		}
		ursl[message.author.id]=reaz;
		await message.react("<a:tick:934091250213212170>");
		return
	}
	
	if(message.mentions.members.size > 0){
		console.log(ursl)
		message.mentions.members.forEach(memb => {
			if (message.guild.id in mhlz){
				if(mhlz[message.guild.id].includes(memb.id)){
					return
				}		
			}
			if(Object.keys(ursl).includes(memb['user']['id'])){
				if (message.content.includes("@everyone") || message.content.includes("@here") ){
					return
				}
				if (ursl[memb['user']['id']]=='defxt360!bo'){
					message.reply(res[Math.floor(Math.random()*res.length)]);
				}else{
					message.reply(ursl[memb['user']['id']]);
				}
				return
			//break;
			}
        })

	if(message.mentions.has(client.user)){
		message.channel.send(res[Math.floor(Math.random()*res.length)]);
	}
	return
	}
};
