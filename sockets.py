import socket
import sys

######################################
# https://www.studytonight.com/network-programming-in-python/socket-methods
##############################
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed with error %s" % (err))

# default port:
port = 4242

# Getting host ip addr
"""try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("There was an error resolving the host")
    sys.exit()"""

# Connecting to the server
s.connect(("localhost", port))
s.send(b"Hello world")
# The 'b' stands for bytes because I kept getting a TypeError: not a bytes-like object being passed.
data = s.recv(1024)
s.close()
print("Received", data)
"""Perhaps it doesn't work properly because I am not 
actually connecting to a server so localhost has
nothing to send back...?
Also, apparently the connection is supposed to be 
short-lived like how HTTP openssh is.
But if you are the server, the connection is longer, 
since you can bind the socket.
But don't know why I cannot type from the server side...?"""
