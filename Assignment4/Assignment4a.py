# Program Name: Assignment4A.py
# Course: IT3883/Section W02
# Student Name: Olu Lamodi
# Assignment Number: Assignment 4
# Due Date: 07/10/2026
# Purpose: This is Program A, the client side of a two program socket
# communication. It asks the user to type in a string, sends it over
# a socket to Program B, then waits for Program B to send it back in
# all uppercase and prints whatever it receives.
# NOTE: Program B needs to be running first before you start this one.
# Resources used: Python docs on socket programming (docs.python.org),
# class notes on network communications.

import socket

# same ip and port that Program B is using
HOST = "127.0.0.1"
PORT = 45000

# ask the user for a string to send
message = input("Enter a string to send to Program B: ")

# create the socket and connect to Program B
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# send the message over
s.send(message.encode())
print("Sent to Program B:", message)

# wait for Program B to send back the uppercase version
response = s.recv(1024)
print("Received back from Program B:", response.decode())

# close the connection
s.close()