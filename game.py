class Game:

    def __init__(self, players):
        self.players = players
        self.board = [[1,1,1,1,1,0,0,0,0,0],
                    [1,1,1,1,0,0,0,0,0,0],
                    [1,1,1,0,0,0,0,0,0,0],
                    [1,1,0,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,2],
                    [0,0,0,0,0,0,0,0,2,2],
                    [0,0,0,0,0,0,0,2,2,2],
                    [0,0,0,0,0,0,2,2,2,2],
                    [0,0,0,0,0,2,2,2,2,2]]
        self.turn = 1
        self.over = True
    
    def start(self):
        self.over = False
        print('''################### GAME BEGINS! ###################''')
        self.printBoard()
        self.progress()

    def printBoard(self):
        line = ""
        for i in range(0, len(self.board)):
            for o in range(0, len(self.board)):
                line = line + str(self.board[i][o])
            print(line)
            line = ""


    def progress(self):
        while not self.over:
            if (self.turn == 1):
                self.board = self.players[0].movement(self.board)
                print("################### PLAYER'S 1 TURN ###################")
                self.printBoard()
                                
                self.turn = 2
            else:
                
                self.board = self.players[1].movement(self.board)
                print("################### PLAYER'S 2 TURN ###################")
                self.printBoard()
                                
                self.turn = 1
    
    def gameOverCheck(self, playerId):
        isZero = False

        count1 = 0
        count2 = 0

        counter = 5
        line = ""
        if (playerId == 1):
            for i in range (0, len(self.board) - counter):
                for o in range(0, len(self.board) - counter):
                    line = line + str(self.board[i][o])
                    if (self.board[i][o] == 1):
                        count1 = count1 + 1
                    elif (self.board[i][o] == 2):
                        count2 = count2 + 1
                    else:
                        isZero = True
                print(line)
                line = ""
                counter = counter + 1
            if (count1 > count2) and not isZero:
                return True
            else:
                return False
        else: 
            for i in range (counter, len(self.board)):
                for o in range(counter, len(self.board)):
                    line = line + str(self.board[i][o])
                    if (self.board[i][o] == 1):
                        count1 = count1 + 1
                    elif (self.board[i][o] == 2):
                        count2 = count2 + 1
                    else:
                        isZero = True
                print(line)
                line = ""
                counter = counter + 1
            if (count1 > count2) and not isZero:
                return True
            else:
                return False
        

                
    

    