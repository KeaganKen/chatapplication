import socket
import threading

nickname = input("Choose a nickname! \n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 55555))


def receive():
    while True:
        try:
            message = s.recv(1024).decode('ascii')
            if message == 'NICK':
                s.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred")
            s.close()
            break

def write():
    while True:
        message = f'{nickname}: {input(" ")}'
        s.send(message.encode('ascii'))







receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

