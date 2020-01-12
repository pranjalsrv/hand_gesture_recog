import socket
from _thread import *


def threaded(c):
    while True:
        try:
            data = c.recv(1024)
            print(c.getpeername(), ': ', str(data)[2:-1])
        except:
            c.close()


host = ""
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print("Socket binded to post", port)
s.listen(5)
print("Socket is listening")
while True:
    c, addr = s.accept()
    print('Connected to :', addr[0], ':', addr[1])
    start_new_thread(threaded, (c,))
s.close()
