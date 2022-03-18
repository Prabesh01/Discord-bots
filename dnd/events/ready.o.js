// module.exports = {
	// name: 'ready',
	// once: true,
	// execute(client) {
		// console.log(`Ready! Logged in as ${client.user.tag}`);
	// },
// };
module.exports = async client => {
	console.log('ready');
        client.user.setStatus('dnd');
	global.ursl={};
	global.shlz={};
	global.chlz={};
	global.mhlz={};
};
