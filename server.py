#!/usr/bin/env python

# Server program

import socket

HOST = ''   #all interfaces
PORT = 7991
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

count = 0
while True:
    data, addr = s.recvfrom(1024)
    if not data: break
    if data == 'EOF':
        break
    else:
        count = count+1
print "Received", count
