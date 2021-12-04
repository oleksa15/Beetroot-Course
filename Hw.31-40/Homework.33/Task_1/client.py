# coding = UTF-8

import socket

HOST = '127.0.0.1'
PORT = 6789
addr = (HOST, PORT)
data = "Hello, Server UDP"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = str.encode(data)
s.sendto(data, addr)
data = bytes.decode(data)
data = s.recvfrom(1024)
print(data)
