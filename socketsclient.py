"""This is a tcp_client.py script."""

# https://www.studytonight.com/network-programming-in-python/socket-methods

import socket

s = socket.socket()
host = socket.gethostname()
port = 9999

s.connect((host, port))
print(s.recv(1024))

s.close()

"""It is normal for this side's connection to automatically 
close after connection"""