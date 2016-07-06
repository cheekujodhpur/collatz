#!/usr/bin/env python

# Server program

import socket
import json

HOST = ''   #all interfaces
PORT = 7991
ADDR = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ADDR)

# Initialize the number
number = 0
with open("limit") as f:
    number = int(f.read())

def request_handler(request):
    global number

    if request["type"] == "CONTROL":
        if request["value"] == "GET":
            # make packet
            packet = {}
            packet["type"] = "DATA"
            packet["value"] = number

            # update current number
            number = number+1

            s.sendto(json.dumps(packet), remote_addr)

        elif request["value"] == "SAVE":
            with open("limit", "w") as f:
                f.write(number)
                f.write("\n")

        elif request["value"] == "INTERRUPT":
            with open("doom", "w") as f:
                f.write(int(request["number"]))
                f.write("\n")

while True:
    # read 1KB of data
    data, remote_addr = s.recvfrom(1024)
    request = json.loads(data)
    
    request_handler(request)
