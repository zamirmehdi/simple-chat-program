import socket
from threading import Thread

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(('localhost', 4422))
name = input('Enter your name: ')
c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())


def send_msg():
    message = input()
    c.send(bytes(message, "utf8"))

    if message == "-quit":
        c.close()
        print('CHAT > Disconnected Successfully!')
        global terminate
        terminate = True


def receive_msg():
    while True:
        try:
            incoming_message = c.recv(1024).decode("utf8")
            print('\n>', incoming_message)
        except OSError:
            break


receiver = Thread(target=receive_msg)
receiver.start()
terminate = False

while True:
    send_msg()
    if terminate:
        break
