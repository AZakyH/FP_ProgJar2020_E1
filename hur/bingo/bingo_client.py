from network import Network
import time

class Client:
    def __init__(self):
        print('init player\n')
        self.player = None
        self.game = None
        self.n = None

        self.GAME_STATE = 1
        self.STATE_WELCOME = 1
        self.STATE_PLAY = 2
        self.STATE_WINNER = 3
        self.count_player = 1
        self.run = True
        self.choice = 0
    
    def start(self):
        print('start\n')
        while self.run:
            if self.GAME_STATE == self.STATE_WELCOME:
                self.handle_welcome()
            elif self.GAME_STATE == self.STATE_PLAY:
                self.handle_play()
            elif self.GAME_STATE == self.STATE_WINNER:
                self.handle_winner()
    
    def handle_welcome(self):
        print('Input 1 untuk mulai bermain dan 2 untuk keluar!')
        command = input()
        if int(command) == 1:
            self.GAME_STATE = self.STATE_PLAY
            self.handle_play()
        else:
            self.run = False
    
    def handle_play(self):
        print('play')
        self.n = Network()
        self.player = int(self.n.getP())
        while self.run:
            try:
                self.game = self.n.send("get")
            except:
                self.run = False
                print("Couldn't get game\n")
                break

            if self.game.bothWent(): #kalo dua-dua dah ngisi 
                self.redrawWindow()
                try:
                    self.game = self.n.send("reset")
                except:
                    self.run = False
                    print("Couldn't get game\n")
                    break

                if (self.game.winner() == 1 and self.player == 1) or (self.game.winner() == 0 and self.player == 0):
                    print("You Won!\n")
                    self.choice = 0
                elif self.game.winner() == -1:
                    print("Tie Game!\n")
                    self.choice = 0
                else:
                    print("You Lost...\n")
                    self.choice = 0

            #kalo belum input tabel
            if not self.game.tables[self.player]:
                ptable = ['0', '0', '0', '0', '0',
                          '0', '0', '0', '0', '0',
                          '0', '0', '0', '0', '0',
                          '0', '0', '0', '0', '0',
                          '0', '0', '0', '0', '0']
                          
                for x in range(1, 26):
                    ngisi = False   #Flag agar bila index yang sudah terpilih tidak terpilih lagi
                    while ngisi == False :
                        print("choose table :")
                        inp = input()
                        if (int(inp) > -1) and (int(inp) < 25):
                            if ptable[int(inp)] == '0':
                                ptable[int(inp)] = str(x)
                                ngisi = True
                            else :
                                print ('Sudah Terisi')
                        else:
                            print('Sel itu gaada')
                try:
                    self.n.sendtable(ptable)
                except:
                    self.run = False
                    print("Couldn't send table\n")
                    break
                
            # print("this is choice: ", self.choice)
            # kalo belum ngirim angka tapi tabel udah
            if self.choice == 0 and self.game.connected():
                print("Input your choosen number!\n")
                self.choice = input()
                if self.player == 0:
                    if not self.game.p1Went:
                        self.n.send(self.choice)
                elif self.player == 1:
                    if not self.game.p2Went:
                        self.n.send(self.choice)
                elif self.player == 2:
                    if not self.game.p3Went:
                        self.n.send(self.choice)
                elif self.player == 3:
                    if not self.game.p4Went:
                        self.n.send(self.choice)
                else:
                    if not self.game.p5Went:
                        self.n.send(self.choice)

            self.redrawWindow()
    
    def handle_winner(self):
        pass

    def redrawWindow(self):
        if not (self.game.connected()):
            print("Waiting for Player...")
            time.sleep(2)
        else:
            move1 = self.game.get_player_move(0)
            move2 = self.game.get_player_move(1)
            if self.game.bothWent():
                # print(move1)
                # print(move2)
                pass
            else:
                if self.game.p1Went and self.player == 0:
                    # print(move1)
                    pass
                elif self.game.p1Went:
                    print("Locked In\n")
                else:
                    # print("Waiting...0")
                    pass
                
                if self.game.p2Went and self.player == 1:
                    # print(move2)
                    pass
                elif self.game.p2Went:
                    print("Locked In")
                else:
                    # print("Waiting...1")
                    pass

if __name__ == "__main__":
    app = Client()
    app.start()