import socket
from _thread import *
import pickle
from game import Game

class Server:
    def __init__(self):
        self.ip = "localhost"
        self.port = 5555
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.ip, self.port))
        self.connected = set()
        self.games = {}
        self.idCount = 0

    def start(self):
        self.s.listen()
        print("Waiting for a connection, Server Started")
        while True:
            conn, addr = self.s.accept()
            print("Connected to:", addr)

            self.idCount += 1
            p = 0
            gameId = (self.idCount - 1) // 2
            if self.idCount % 2 == 1:
                self.games[gameId] = Game(gameId)
                print("Creating a new game...")
            else:
                self.games[gameId].ready = True
                p = 1

        start_new_thread(self.threaded_client, (conn, p, gameId))

    def threaded_client(self, conn, p, gameId):
        conn.send(str.encode(str(p)))
        reply = ""
        while True:
            try:
                data = conn.recv(4096).decode()

                if gameId in self.games:
                    game = self.games[gameId]

                    if not data:
                        break
                    else:
                        if data == "reset":
                            game.resetWent()
                        elif data != "get":
                            game.play(p, data)

                        conn.sendall(pickle.dumps(game))
                else:
                    break
            except:
                break

        print("Lost connection")
        try:
            del self.games[gameId]
            print("Closing Game", gameId)
        except:
            pass
        self.idCount -= 1
        conn.close()


if __name__ == '__main__':
    server = Server()
    server.start()