import socket
import multiprocessing


def boot():
    def encrypt(text, s):
        result = ""
        for i in range(len(text)):
            char = text[i]

            if char.isupper():
                result += chr((ord(char) + s - 65) % 26 + 65)

            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result

    HOST = '127.0.0.1'
    PORT = 65432 

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = encrypt('Hello world', 4)
        s.sendall(bytes(message, 'ascii'))
        data = s.recv(1024)

    print('Received', data)


def main():
    client = multiprocessing.Process(target=boot)
    client.start()
    client.join()


if __name__ == '__main__':
    main()

