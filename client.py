#!/usr/bin/env python

# Client program

import socket
import json
import sys

HOST = sys.argv[1]   # The remote host
PORT = 7991          # The same port as server
ADDR = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def is_collatz(num):
    numo = num
    tmp = []
    while num != 1:
        tmp.append(num)
        if num%2 == 0:
            num = num/2
        else:
            num = num*3 + 1
        if num in tmp:
            return False

        # assume all smaller numbers are checked
        if num < numo:
            return True
    return True

def get_number():
    # generate initial packet
    packet = {}
    packet["type"] = "CONTROL"
    packet["value"] = "GET"

    # send
    s.sendto(json.dumps(packet), ADDR)
    # await response
    reply, comm_addr = s.recvfrom(1024)
    response = json.loads(reply)

    if response["type"] == "DATA":
        left,right = int(response["left"]), int(response["right"])
        for number in range(left, right+1):
            if not is_collatz(number):
               send_interrupt(number) 

    return

def send_interrupt(number):
    # generate packet
    packet = {}
    packet["type"] = "CONTROL"
    packet["value"] = "INTERRUPT"
    packet["num"] = number
    s.sendto(json.dumps(packet), ADDR)

while True:
    get_number()
