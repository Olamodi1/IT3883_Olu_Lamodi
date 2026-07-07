# Program Name: Assignment4B.py
# Course: IT3883/Section W02
# Student Name: Olu Lamodi
# Assignment Number: Assignment 4
# Due Date: 07/10/2026
# Purpose: This is Program B, the server side of a two program socket
# communication. It listens for a string sent over the network from
# Program A, converts it to all uppercase, prints it, then sends it
# back to Program A. This program needs to be started first before
# running Program A.
# Resources used: Python docs on socket programming (docs.python.org),
# class notes on network communications.

import socket

# the ip and port we are going to listen on
# 127.0.0.1 just means this same computer (localhost)
HOST = "127.0.0.1"
PORT = 45000

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# this lets us reuse the port right away if we restart the program
# without it you sometimes get a "port already in use" error
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind to the address and port and start listening
s.bind((HOST, PORT))
s.listen()
print("Program B is listening on port", PORT)

# wait for Program A to connect
conn, addr = s.accept()
print("Got a connection from", addr)

# receive the message from Program A (up to 1024 bytes)
data = conn.recv(1024)
received = data.decode()
print("Received from Program A:", received)

# convert it to uppercase
upper = received.upper()
print("Sending back uppercase:", upper)

# send the uppercase version back to Program A
conn.send(upper.encode())

# close the connection
conn.close()
s.close()