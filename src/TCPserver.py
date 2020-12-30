#!/usr/bin/env python

import socket

# make socket object; don't need to specify AF_INET & SOCK_STREAM since they're defaults
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get hostname (IPv4 address of host as a string)
host = socket.gethostname()

# set the port
port = 444

# message to confirm server is starting and give the address:port
print("Starting server at %s:%d" % (host, port))

# bind; needs an address; AF_INET does this with a list of (host, port)
serversocket.bind((host, port))

# start listening; optional 'backlog', number of connections that can be accepted
serversocket.listen(3)

while True:
    # get socket object and address from the incoming client
    clientsocket, address = serversocket.accept()
    # print (log) that connection has been received
    print("Received connection from %s" % str(address))
    # make the message and send it
    message = "Thank you for connecting to the server\r\n"
    clientsocket.send(message.encode('ascii'))
    # close the client connection
    clientsocket.close()