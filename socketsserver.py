"""This is a tcp_server.py script"""

# https://www.studytonight.com/network-programming-in-python/socket-methods

import socket

s = socket.socket()
host = socket.gethostname()
port = 9999

s.bind((host, port))

print("Waiting for connection...")
s.listen(5)

while True:
    conn, addr = s.accept()
    print("Got connection from ", addr)
    conn.send("Server saying Hi".encode())
    # .encode() converts the string into bytes which
    # enables the 'conn.send' fn to work.
    # Alternative is is to put 'b'"Got connection..."
    conn.close()

    #WHAT THE FUCK IS CONN??  I haven't declared it??
