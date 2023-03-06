# https://www.geeksforgeeks.org/socket-programming-python/

"""
Socket programming is a way of connecting two nodes on a network to communicate with
 each other. One socket(node) listens on a particular port at an IP, while the
 other socket reaches out to the other to form a connection.
 The server forms the listener socket while the client reaches out to the server.

"""

import socket

s = socket.gethostbyname('www.google.com')

print(s)          # 142.251.42.4



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
Here we made a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is
 SOCK_STREAM. AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol. 
"""

print(s)                    # <socket.socket fd=452, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>


###############
## EXAMPLE 1:
###############

# An example script to connect to Google using socket
# programming in Python
import socket  # for socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % (err))

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

    # this means could not resolve the host
    print("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print("the socket has successfully connected to google")

