from pyrcb import IRCBot
import simplejson as json

IRC_network 	= "irc.snoonet.org"
IRC_port 	= 6667
IRC_channel	= "#deitrebukkenenoobs-dev"
bot_name 	= "Kadbot"
commands_path	= "/home/kad/Projects/IRC_Botwars/commands.json"


# Main fucntion
def main():
    bot = MyBot()
    bot.connect(IRC_network, IRC_port)
    bot.register(bot_name)
    bot.join(IRC_channel)
    bot.listen()

# This is the bot, and all it's commands and functions
class MyBot(IRCBot):

	def private_msg(self, nickname, message):
		self.send(nickname, message)

	def public_msg(self, message):
		self.send(IRC_channel, message)

	def on_message(self, message, nickname, channel, is_query):
		print(message)
        	if message[0] == "!":
			message = message.replace("!","")
			commands = message.split(" ")
			self.execute_command(commands)

	def execute_command(self, commands):
		json_com = json.load(open(commands_path))
		
		self.public_msg(str(json_com.get(commands[0]).get(commands[1])))

		#print(json_com['test'])
	 

# Start main function
if __name__ == "__main__":
	main()

