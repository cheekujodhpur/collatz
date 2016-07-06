#!/usr/bin/env python

# Server program

import socket

HOST = ''   #all interfaces
PORT = 7991
s = socket.socket(socket.AF_INET, socket.sock_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()
