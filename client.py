#!/usr/bin/env python

# Client program

import socket
import struct
import sys

HOST = '127.0.0.1'   # The remote host
PORT = 7991          # The same port as server
ADDR = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

count = 0
for i in range(1000000):
    s.sendto(struct.pack('<L', sys.getsizeof(str(i))), ADDR)
    s.sendto(str(i), ADDR)
    count = count+1

print "Sent", count
s.sendto(struct.pack('<L', 0), ADDR)
