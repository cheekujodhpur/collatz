#!/usr/bin/env python

# Client program

import socket

HOST = 'wncc-iitb.org'   # The remote host
PORT = 7991              # The same port as server
s = socket.socket(socket.AF_INET, socket.sock_STREAM)
s.connect((HOST, PORT))
s.send(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))
