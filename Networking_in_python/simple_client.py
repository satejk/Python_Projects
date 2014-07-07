#!/usr/bin/python 

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port = 15454

s.connect((host,port))

print s.recv(1024)
print "This is so cool"
s.send(raw_input(" enter your name"))

s.close()
