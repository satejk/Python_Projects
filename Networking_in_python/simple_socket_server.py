#!/usr/bin/python #This is server.py 

# Author: SATEJ KHANDEPARKAR
# MASTERS IN EMBEDDED AND INTELLIGENT SYSTEMS 
# HALMSTAD UNIVERSITY, SWEDEN

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port = 12345

s.bind((host,port))

s.listen(5)

while True:
	c, addr = s.accept()
	print "Got Connection From",addr
	c.send("Thank you for connecting \n")
	c.send("Can you provide your name \n")
	s.listen(3)
	a = s.accept()
	print "your name is \n", a
	
	c.close()
