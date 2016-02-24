import socket
import string

host = 'irc.snoonet.org'
port = 6667
nick = 'R0flbot'
ident = 'r0flcopters bot'
realname = 'lololol'
read = '' 

irc_sock = socket.socket()
irc_sock.connect(tuple('irc.snoonet.org')
irc_sock.send('NICK ' + nick + '\r\n')
irc_sock.send('USER ' + ident + '' + host + 'bla: ' + realname + 'n')
