class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.p3Went = False
        self.p4Went = False
        self.p5Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None, None, None, None]
        self.p1Table = False
        self.p2Table = False
        self.p3Table = False
        self.p4Table = False
        self.p5Table = False
        self.tables = [None, None, None, None, None]
        self.wins = [0,0]
        self.ties = 0
        self.size = 5
        self.table = [] 

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def get_player_table(self, p):
        return self.tables[p]

    def setTable(self, player, table):
        self.tables[player] = table
        if player == 0:
            self.p1Table = True
        elif player == 1:
            self.p2Table = True
        elif player == 2:
            self.p3Table = True
        elif player == 3:
            self.p4Table = True
        elif player == 4:
            self.p5Table = True
    
    def play(self, player, move):
        self.moves[player] = move
        print(self.moves[player])
        if player == 0:
            self.p1Went = True
        elif player == 1:
            self.p2Went = True
        elif player == 2:
            self.p3Went = True
        elif player == 3:
            self.p4Went = True
        elif player == 4:
            self.p5Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):

        # p1 = self.moves[0].upper()[0]
        # p2 = self.moves[1].upper()[0]

        winner = -1
        # if p1 == "R" and p2 == "S":
        #     winner = 0
        # elif p1 == "S" and p2 == "R":
        #     winner = 1
        # elif p1 == "P" and p2 == "R":
        #     winner = 0
        # elif p1 == "R" and p2 == "P":
        #     winner = 1
        # elif p1 == "S" and p2 == "P":
        #     winner = 0
        # elif p1 == "P" and p2 == "S":
        #     winner = 1

        return winner

    # def resetWent(self):
    #     self.p1Went = False
    #     self.p2Went = False