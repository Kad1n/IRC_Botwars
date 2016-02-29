from pyrcb import IRCBot


class MyBot(IRCBot):
    def on_message(self, message, nickname, channel, is_query):
        if is_query:
            self.send(nickname, "You said: " + message)
        elif message == "!penis":
            self.send(channel, nickname + " wanted the " + "penis command")

    def on_join(self, nickname, channel):
        if nickname != self.nickname:
            self.send(channel, nickname + " has joined " + channel)


def main():
    bot = MyBot()
    bot.connect("irc.snoonet.org", 6667)
    bot.register("Roflbot")
    bot.join("#dei3bukkenenoobs")
    bot.listen()


if __name__ == "__main__":
    main()
