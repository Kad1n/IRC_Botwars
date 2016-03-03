from pyrcb import IRCBot


class MyBot(IRCBot):
    def on_message(self, message, nickname, channel, is_query):
        if is_query:
            self.send(nickname, "You said: " + message)
        elif message == "!penis":
            self.send(channel, nickname + ": " + "penis command")
        elif message == "!hestepikk":
            self.send(channel, nickname + ": " + "hestepikk command")
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
                      ": " + "https://www.youtube.com/watch?v=a8c5wmeOL9o&ab_channel=Dylancliff111")
        elif message == "!stallman":
            self.send(channel, nickname +
                      ": " + "https://www.youtube.com/watch?v=Dn8gealMDsg&ab_channel=Skirmant")
        elif message == "!offandon":
            self.send(channel, nickname +
                      ": " + "http://www.myinstants.com/media/sounds/it.mp3")
        elif message == "!406":
            self.send(channel, nickname +
                      ": " + "http://www.myinstants.com/media/sounds/lemon-grab-unacceptable.mp3")

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
