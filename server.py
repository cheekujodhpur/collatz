#!/usr/bin/env python

# Server program

import socket
import struct

HOST = ''   #all interfaces
PORT = 7991
ADDR = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ADDR)

count = 0
while True:
    # read the header, size of incoming number
    try:
        num_len = struct.unpack('<L', s.recvfrom(struct.calcsize('<L'))[0])[0]
    except ValueError:
        print "Corrupt header"

    data, remote_addr = s.recvfrom(num_len)
    print data
    if data.isdigit(): count = count + 1
print "Received", count
