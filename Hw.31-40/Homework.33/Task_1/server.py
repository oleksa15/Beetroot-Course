# coding = UTF-8

import socket

HOST = '127.0.0.1'
PORT = 6789
addr = (HOST,PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)


while True:

    data, addr = sock.recvfrom(1024)
    print('client addr: ', addr)
    print(data)
    sock.sendto(data.upper(), addr)
