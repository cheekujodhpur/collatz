#!/usr/bin/env python

# Client program

import socket

HOST = '127.0.0.1'   # The remote host
PORT = 7991              # The same port as server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

count = 0
for i in range(1000000):
    s.sendto(str(i), (HOST, PORT))
    count = count+1

print "Sent", count
s.sendto('EOF', (HOST, PORT))
s.close()
