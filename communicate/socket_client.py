import socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 9009

class Socket_client():

    def __init__(self):
        pass

    def rcvMsg(self, sock):
        while True:
            try:
                data = sock.recv(1024)
                if not data:
                    break
                print(data.decode())
            except Exception as e:
                print(e)

    def runChat(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            t = Thread(target=self.rcvMsg, args=(sock,))
            t.daemon = True
            t.start()

            while True:
                msg = input()
                if msg == '/quit':
                    sock.send(msg.encode())
                    break
                sock.send(msg.encode())