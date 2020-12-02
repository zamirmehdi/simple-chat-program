import socket
from threading import Thread

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(('localhost', 4422))
name = input('Enter your name: ')
c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())


def send_msg():
    # //message = sys.stdin.readline()
    message = input('\n> ')

    if message == "-exit":
        c.close()
        print('CHAT >  Disconnected Successfully!')
    else:
        c.send(bytes(message, "utf8"))


def receive_msg():
    while True:
        try:
            incoming_message = c.recv(1024).decode("utf8")
            print('\n> ', incoming_message)
        except OSError:
            break


receiver = Thread(target=receive_msg)
receiver.start()

while True:
    send_msg()
