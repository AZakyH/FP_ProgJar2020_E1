import socket
import select
import sys
import threading
import os
import time
# from math import *

BUFFER_SIZE = 2048

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = '127.0.0.1'
port = 8082
server.bind((ip_address, port))
server.listen(100)
list_of_clients = []


def clientthread(conn, addr):
    while True:
        try:
            # print("coba")
            pilihan = conn.recv(BUFFER_SIZE).decode()
            
            tandaMat = int("1")
            tandaChat = int("2")
            tandaFile = int("3")

            if int(pilihan) == int(tandaMat):
                print("Operasi Matematika")
                message = conn.recv(BUFFER_SIZE).decode()
                message = message.rstrip()
                hasil = eval(message)
                sd = " = "
                message = str(message) + str(sd) + str(hasil)
                print("hasil : ", message)
                broadcastChatMat(message, conn, pilihan)

            elif int(pilihan) == int(tandaChat):
                print("Proses Chat")
                message = conn.recv(BUFFER_SIZE).decode()
                message = message.rstrip()
                broadcastChatMat(message, conn, pilihan)

            elif int(pilihan) == int(tandaFile):
                print("Melakukan BC file")
                message = conn.recv(BUFFER_SIZE).decode()
                filename, filesize = message.split()
                print(filename, filesize)
                conn.send("Ok".encode())
                data = conn.recv(int(filesize))
                print('<' + addr[0] + '> ' + "sending")
                
                broadcastFile(data, conn, filename, filesize, pilihan)
                
            else:
                remove(conn)
            
        except:
            continue

def broadcastChatMat(message, connection, pilihan):
    for clients in list_of_clients:
        if clients != connection:
            clients.sendall((pilihan.encode()))
            print("data pilihan terkirim")
            time.sleep(2)

            clients.sendall((message.encode()))
            time.sleep(2)
            print("data hasil operasi matematika / Chat terkirim")

def broadcastFile(message, connection, filename, filesize, pilihan):
    for clients in list_of_clients:
        if clients != connection:
            try:
                # print("Proses BC file")
                # print(pilihan, "sebelum bc")
                clients.send((pilihan.encode('utf-8')))
                time.sleep(2)
                print("data pilihan terkirim")

                clients.send(f"{pilihan} {filename} {filesize}".encode('utf-8'))
                print("data file terkirim")
                
                time.sleep(2)
                # print(clients.recv(BUFFER_SIZE).decode('utf-8'))
                clients.sendall(message)
                time.sleep(2)
                print("Proses BC File Selesai")
                   
            except:
                clients.close()
                remove(clients)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

conn = None
while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + ' connected')
    threading.Thread(target=clientthread, args=(conn, addr)).start()
    # print("coba")

conn.close()
