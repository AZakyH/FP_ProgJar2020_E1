import socket
from _thread import *
import pickle
from game import Game

server = '0.0.0.0'
port = 5537

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            rawdata = conn.recv(4096)

            # print("terima pickle")
            pidata = pickle.loads(rawdata)
            # print("selesai pickle")

            if isinstance(pidata, list):
                data = str(pidata[0][0])
            else:
                data = pidata
                
            if gameId in games:
                # print("gameId ada")
                game = games[gameId]
                print("data: " + data)
                if data == "table":
                    print("data == table")
                    try:
                        game.setTable(p, pidata[1])
                    except:
                        print("game gagal nge set table")

                if not data:
                    print("data ga ada")
                    break
                else:
                    # print("lanjoot")

                    if data == "reset":
                        game.resetWent()
                    elif data != "get": 
                        print("Apakah ke sini?")
                        game.play(p, data)
                        
                    try:
                        conn.sendall(pickle.dumps(game))
                        print("berhasil send game ke client")
                    except:
                        print("gagal kirim game ke client")
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))