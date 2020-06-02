###################################################### Make Table
box_tmp = None
def set_box(box, box_pos, holder_pos):
    global box_tmp

    if box_pos[0] == holder_pos[0]:
        box_tmp = box
        return True
    else :
        box_tmp = None
        return False

def makeTable(str1, str2):
    posisi = int(str1)-1
    row = int(posisi/5)
    col = posisi - (row * 5)
    row = row + 1
    col = col + 1
    val = int(str2)

    table[row][col] = val

def get_box():
    return box_tmp
###################################################### Game Variable
import random

gameOver = False
jumlahUser = 0
tableDone = 0
f = False
bingo_point = 0
key = ""
update_status = False
box_name = ""
box_val = ""
username = ""

def getJumlahUser():
    sendJumlahUser()
    return str(jumlahUser)

def getJumlahTableDone():
    global f
    sendJumlahTableDone()
    while f == False:
        print()
    f = False
    return str(tableDone)

def getKey():
    return key

def getBoxName():
    return box_name

def getBoxVal():
    return box_val

def setBingoPoint():
    global bingo_point
    bingo_point = bingo_point + 1

def getBingoPoint():
    return str(bingo_point)

def setGameOver():
    global gameOver
    gameOver = False

def getGameOver():
    return gameOver

def setUpdateStatus():
    global update_status
    update_status = False

def getUpdateStatus():
    return update_status

def getUsername():
    return username

table = [[0 for i in range(6)] for j in range(6)]
map_table = [[0 for i in range(2)] for i in range(26)]
bingo_table = [[0 for i in range(6)] for j in range(6)]

def cek_table_kosong():
    for i in range(1,6):
            for j in range(1,6):
                if table[i][j] == 0:
                    return False
    return True

def rand_table():
    a_list = list(range(1, 26))
    random.shuffle(a_list)

    tmp = 0
    for i in range(1,6):
        for j in range(1,6):
            table[i][j] = a_list[tmp]
            tmp = tmp + 1

def tablecek():
    for i in range(1,6):
        for j in range(1,6):
            if table[i][j] == 0:
                return False
    return True
    
def init_table():
    global gameOver
    gameOver = False

    if tablecek() == False:
        tmp = 1
        for i in range(1,6):
            for j in range(1,6):
                table[i][j] = tmp
                tmp = tmp + 1

    for i in range(1,6):
        for j in range(1,6):
            map_table[table[i][j]][0] = i
            map_table[table[i][j]][1] = j

            bingo_table[i][j] = 0
    
def cekBingo():
    for i in range(1,6):
        flag1 = True
        flag2 = True 
        for j in range(1,6):
            if bingo_table[i][j] == 0:
                flag1 = False
            if bingo_table[j][i] == 0:
                flag2 = False

        if flag1 or flag2:
            return True
    return False

def update_table(str1):
    val = int(str1)
    row = map_table[val][0] 
    col = map_table[val][1]
    bingo_table[row][col] = 1

    # print(bingo_table)

    flag = True
    for i in range(1,6):
        if bingo_table[i][col] == 0:
            flag = False
    if flag:
        return True

    flag = True
    for i in range(1,6):
        if bingo_table[row][i] == 0:
            flag = False
    return flag
###################################################### Socket Client
import socket
import select
import sys
import msvcrt
import os
import math
import threading

###########################################################
server = None
def sendBingo():
    message = "bingo\n"
    print("bingo")
    server.send(message.encode())

def sendNomor(str1):
    global key
    message = "nomor " + str1 + '\n'
    server.send(message.encode())
    server.send(key.encode())
    key = ""

def sendJumlahUser():
    message = "jumlahUser\n"
    server.send(message.encode())

def sendJumlahTableDone():
    message = "jumlahTableDone\n"
    server.send(message.encode())

def sendTableDone():
    message = "tableDone\n"
    server.send(message.encode())

def sendTableReset():
    message = "tableReset\n"
    server.send(message.encode())
###########################################################
def join_thread(ip_tmp, username_tmp):
    global server, jumlahUser, tableDone, key, update_status, box_name, box_val, gameOver, username, f
    username = "username_tmp"

    login_flag = 1
    ip = ip_tmp
    username = username_tmp

    # jika login ftp berhasil lakukan koneksi ke server
    if(login_flag):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 8081
        server.connect((ip, port))

        while True:
            socket_list = [server]
            read_socket, write_socket, error_socket = select.select(socket_list, [], [], 1)

            for socks in read_socket:
            
                if socks == server:
                    message = socks.recv(1024).decode()
                    messages = []
                    messages = message.split('\n')

                    for message in messages:
                        if message == '':
                            continue
                        print(message)
                        print("----------------------------------")
                        
                        #  mendapatkan perintah dengan melakukan split
                        try :
                            choice, nama = message.split()
                        except:
                            choice = message

                        if (choice == 'jumlahUser'):
                            jumlahUser = int(nama)
                        elif (choice == 'jumlahTableDone'):
                            tableDone = int(nama)
                            f = True
                        elif (choice == 'bingo'):
                            if cekBingo() == False:
                                gameOver = True
                        elif (choice == 'key'):
                            key = nama
                            # print("Key -> ", key)
                        elif (choice == 'nomor'):
                            val = int(nama)
                            # print ("Val :", val)
                            row  = map_table[val][0]
                            col  = map_table[val][1]

                            update_status = True
                            tm = str((row-1)*5+col)
                            box_name = "box_"+tm
                            box_val = nama
                            # print ("Box :", box_name)
                            bingo_table[row][col] = 1
                        
        server.close()

def join(ip_tmp, username_tmp):
    threading.Thread(target = join_thread, args = (ip_tmp, username_tmp)).start()