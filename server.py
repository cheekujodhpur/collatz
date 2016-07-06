#!/usr/bin/env python

# Server program

import socket
import struct

HOST = ''   #all interfaces
PORT = 7991
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

count = 0
while True:
    num_len = struct.unpack('<L', s.recvfrom(struct.calcsize('<L'))[0])[0]
    if num_len == 0: break
    data, addr = s.recvfrom(num_len)
    if data.isdigit(): count = count + 1
print "Received", count
