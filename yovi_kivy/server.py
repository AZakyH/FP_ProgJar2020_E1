import socket
import select
import sys
import threading
import math
import os
import zipfile
import uuid
import time

turn = 0
key = str(uuid.uuid1())
jumlahUser = 0
tableDone = 0

# membuat socket pada server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = '127.0.0.1'
port = 8081
server.bind(("localhost", 8081))
server.listen(100)
list_of_clients = []

def getNum(str1):
    return int(str1.replace(" ", ""))

# menghandle client
def clientthread(conn, addr):
    global key, turn, tableDone

    message = "connected"
    conn.send(message.encode())
    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
                message = str(message)

                messages = []
                messages = message.split('\n')

                for message in messages:
                    if message == '':
                        continue

                    # Mendapatkan perintah dengan di split -> choice
                    try:
                        choice, nama = message.split()
                    except:
                        choice = message

                    if (choice == 'jumlahUser'):
                        message = 'jumlahUser ' + str(jumlahUser) + '\n'
                        conn.send(message.encode())
                    elif (choice == 'jumlahTableDone'):
                        message = 'jumlahTableDone ' + str(tableDone) + '\n'
                        conn.send(message.encode())
                    elif (choice == 'tableDone'):
                        tableDone = tableDone + 1
                    elif (choice == 'tableReset'):
                        tableDone = 0
                    elif (choice == 'bingo'):
                        print("bingo")
                        message = 'bingo' + '\n'
                        broadcast(message, conn)
                    elif (choice == 'nomor'):
                        ky = conn.recv(1024).decode()
                        if key == ky:
                            message = 'nomor ' + nama + '\n'
                            broadcast(message, conn)
                            turn = turn + 1
                            if turn > jumlahUser-1:
                                turn = 0
                            key = str(uuid.uuid1())
                            message = 'key ' + key + '\n'
                            list_of_clients[turn].send(message.encode())
                    else:
                        message_to_send = '<' + addr[0] + '> ' + message + '\n'
                        broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        jumlahUser = jumlahUser - 1
        list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)

    jumlahUser = jumlahUser + 1
    if jumlahUser == 1:
        message = 'key ' + key
        conn.send(message.encode())

    print(addr[0] + ' connected')
    # masing client akan di handle oleh sebuah thread
    threading.Thread(target = clientthread, args = (conn, addr)).start()

conn.close()