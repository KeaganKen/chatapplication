import socket
import threading
host = '127.0.0.1'
port = 55555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} has left the chat!'.encode('ascii'))
            break

def receive():
    while True:
        client, address = s.accept()
        print(f'Connecting with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f'Nickname of the client is {nickname}!\n')
        broadcast(f'{nickname} joined the chat!\n'.encode('ascii'))
        client.send('Connected to the server \n'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('server is listening')
receive()