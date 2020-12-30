#!/usr/bin/env python

import socket

# make (client) socket object; again the AF_INET and SOCK_STREAM are defaults
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get address of host
host = socket.gethostname()

# pre-defined port
port = 444

# connect the client and message (log) that this has happened
clientsocket.connect((host, port))
print("Client connecting on %s:%d" % (host, port))

# store incoming; define the max buffer size that we can receive
message = clientsocket.recv(1024)

# don't need the client any more (have stored message) so close
clientsocket.close()

# we know message is ascii-encoded
print("Message received: %s" % message.decode('ascii'))
