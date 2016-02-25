#!/usr/bin/env python

import socket
import string

host = 'irc.snoonet.org'
port = 6667
nick = 'R0flbot'
ident = 'r0flcoptersbot'
realname = 'lololol'
read = ''

irc_sock = socket.socket()
irc_sock.connect(("irc.snoonet.org", port))
irc_sock.send('NICK ' + nick + '\r\n')
irc_sock.send('USER ' + ident + '' + host + 'bla: ' + realname + 'n')


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
