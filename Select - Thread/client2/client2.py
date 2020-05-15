import socket
import select
import sys
import msvcrt
import time
import os
# from math import *

BUFFER_SIZE = 2048
filename = ""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8082
server.connect((ip_address, port))
while True:
    socket_list = [server]
    read_socket, write_socket, error_socket = select.select(socket_list, socket_list, [])
    if msvcrt.kbhit():
        read_socket.append(sys.stdin)
        # read_socket.insert(0, sys.stdin)

    for socks in read_socket:
        tandaMat = int("1")
        tandaChat = int("2")
        tandaFile = int("3")
        # nerima file dari server
        if socks == server:
            print("Client menerima sesuatu dari server")
            pilihan = socks.recv(BUFFER_SIZE).decode('utf-8')

            message = socks.recv(BUFFER_SIZE).decode('utf-8')
            
            if int(pilihan) == tandaMat or int(pilihan) == tandaChat:
                if (int(pilihan) == tandaMat) : 
                    print("Operasi matematika")
                elif int(pilihan) == tandaChat:
                    print("Menerima chat")
                print(message)
                continue

            if str(message):
                print("Menerima File")
                x, filename, filesize = message.split()
                print(x)
                # print("x sudah")
                print(filename)
                # print("file name sudah")
                print(filesize)
                # print("filesize sudah")
                socks.send("Ok".encode('utf-8'))
                data = socks.recv(int(filesize))
                with open(filename, 'wb') as openFile:
                    openFile.write(data)
    
        # ngirim file dari client skrg
        else:
            pilihan = str(sys.stdin.readline())
            print("Client mengirim sesuatu ke server")
            
            if int(pilihan) == tandaMat or int(pilihan) == tandaChat:
                if (int(pilihan) == tandaMat) : 
                    print("Akan melakukan operasi matematika")
                elif int(pilihan) == tandaChat:
                    print("Akan mengirim chat")
                server.send(pilihan.encode())
                teks = sys.stdin.readline()
                server.send(teks.encode())
                
                if (int(pilihan) == tandaMat) :
                    sys.stdout.write('<Operasi Matematika> ')
                elif int(pilihan) == tandaChat:
                    sys.stdout.write('<Isi Chat> ')
                
                sys.stdout.write(teks)
                sys.stdout.write("\n")

            elif int(pilihan) == tandaFile:
                print("Akan mengirim file")
                server.send(pilihan.encode())
                filename = sys.stdin.readline()
                filename = filename.strip('\n')
                filesize = os.path.getsize(filename)
                server.send(f"{filename} {filesize}".encode())
                print(server.recv(BUFFER_SIZE).decode())
                
                with open(filename, "rb") as openFile:
                    while True:
                        bytes_read = openFile.read(filesize)
                        if not bytes_read:
                            break
                        server.sendall(bytes_read)

                sys.stdout.write('<Nama File> ')
                sys.stdout.write(filename)
                sys.stdout.write("\n")
            sys.stdout.flush()

server.close()
