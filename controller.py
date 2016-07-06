#!/usr/bin/env python

# Controller program program

import socket
import json
import time

HOST = '127.0.0.1'   # The server
PORT = 7991          # The same port as server
ADDR = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_save():
    # generate packet
    packet = {}
    packet["type"] = "CONTROL"
    packet["value"] = "SAVE"
    s.sendto(json.dumps(packet), ADDR)
    time.sleep(10)
    send_save()

send_save()
