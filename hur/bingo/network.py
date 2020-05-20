import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server = '157.245.50.224'
        self.server = '127.0.0.1'
        self.port = 5537
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            # self.client.send(str.encode(data))
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)

    def sendtable(self, table):
        try:
            # print("masuk sendtable")
            data = [["table"], table]
            # print(data[0][0])
            try:
                self.client.sendall(pickle.dumps(data))
            except:
                print("Couldn't send data")
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)