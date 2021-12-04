# coding = UTF-8

import socket
import json

HOST = '127.0.0.1'
PORT = 6789
addr = (HOST,PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)

def encypt_func(txt, s):
    result = ""
    for i in range(len(txt)):
        char = txt[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 64) % 26 + 65)
        else:
            result += chr((ord(char) + s - 96) % 26 + 97)
    return result

while True:

    data, addr = sock.recvfrom(1024)
    print('client addr: ', addr)
    data = bytes.decode(data)
    data = json.loads(data)
    text = data[0]
    key = data[1]
    text = str.encode(encypt_func(text, key))
    print(text)
    sock.sendto(text, addr)