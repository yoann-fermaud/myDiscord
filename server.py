import socket
import threading

HOST = '127.0.0.1'
PORT = 9000


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))  # Ouverture du port
        self.server.listen()

        self.clients = []
        self.nicknames = []

        print("Server is running")
        self.receive()

    # broadcast : send message to all the connected clients
    def broadcast(self, msg):
        for client in self.clients:
            client.send(msg)

    # handle : handle all connections
    def handle(self, client):
        while True:
            try:
                self.message = client.recv(1024)
                # print(f'{self.nicknames[self.clients.index(client)]}')
                self.broadcast(self.message)
            except:
                self.index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                # self.nickname = self.nicknames[self.index]
                # self.nicknames.remove(self.nickname)
                break

    # receive : accept new connection
    def receive(self):
        while True:
            self.client, self.address = self.server.accept()
            print(f"Connected with {str(self.address)}")

            self.client.send("TEST".encode('utf-8'))
            # self.nickname = self.client.recv(1024)

            self.clients.append(self.client)
            # self.nicknames.append(self.nickname)

            # print(f"Nickname of the client : {self.nickname}")
            # self.broadcast(f"{self.nickname} is connected to the server\n".encode('utf-8'))
            # self.client("Connected to the server".encode('utf-8'))

            self.thread = threading.Thread(target=self.handle,
                                           args=(self.client,))  # We put a coma to have a tuple and not a string
            self.thread.start()


server = Server()
