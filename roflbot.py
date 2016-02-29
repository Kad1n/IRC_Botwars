from pyrcb import IRCBot
# import redis
# import parse

# import config


class infobot(IRCBot):
    def on_message(self, message, nickname, channel, is_query):
        if is_query:
            self.send(nickname, "You said: " + message)
        else:
            self.send(channel, nickname + " said :" + message)

    def on_join(self, nickname, channel):
        if nickname != self.nickname:
            self.send(channel, nickname + " has joined " + channel)


def main():
    bot = MyBot()
    bot.connect("irc.snoonet.org", 6667)
    bot.register("mybot")
    bot.join("#dei3bukkenenoobs")
    bot.listen()


if __name__ == "__main__":
    main()
