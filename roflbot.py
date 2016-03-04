from pyrcb import IRCBot
import sqlite3

# Making some variables to shorten things down, and what db to use
conn = sqlite3.connect('rolfbot.db')
c = conn.cursor()


# Just some variables to shorten down some commands, somewhat temporary
noice = "https://www.youtube.com/watch?v=a8c5wmeOL9o&ab_channel=Dylancliff111"
stallman = "https://www.youtube.com/watch?v=Dn8gealMDsg&ab_channel=Skirmant"
unnaccept = "http://www.myinstants.com/media/sounds/lemon-grab-unacceptable.mp3"


# This is the bot, and all it's commands and functions
class MyBot(IRCBot):
    def on_message(self, message, nickname, channel, is_query):
        if is_query:
            self.send(nickname, "You said: " + message)
        elif message == "!approve":
            if nickname == "r0flcopt3r" or nickname == "kad" or \
                    nickname == "moggy":
                self.send(channel, nickname + ": " + "kad-server.net/" +
                          nickname + "approves")
            else:
                self.send(channel, nickname + "kad-server.net/approves")
        elif message == "!lies":
            self.send(channel, nickname +
                      ": " + "https://www.youtube.com/watch?v=YWdD206eSv0")
        elif message == "!pirate":
            self.send(channel, nickname +
                      ": " + "http://cristgaming.com/pirate.swf")
        elif message == "!noice":
            self.send(channel, nickname +
                      ": " + noice)
        elif message == "!stallman":
            self.send(channel, nickname +
                      ": " + stallman)
        elif message == "!offandon":
            self.send(channel, nickname +
                      ": " + "http://www.myinstants.com/media/sounds/it.mp3")
        elif message == "!406":
            self.send(channel, nickname +
                      ": " + unnaccept)

    # Making a function for storing quotes
    def quote():
        # creates the table if it doesn't already exsist
        c.execute('''CREATE TABLE IF NOT EXISITS quote
                  (nickname text, message text, number INTEGER)''')

        # Grabbing command, and stores it in the database
        if message == "!quote":
            c.execute("INSERT INTO quote VALUES(nickname, message)")


# Main fucntion
def main():
    bot = MyBot()
    bot.connect("irc.snoonet.org", 6667)
    bot.register("Roflbot")
    bot.join("#dei3bukkenenoobs")
    bot.listen()


# Start main function
if __name__ == "__main__":
    main()
