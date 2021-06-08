from mcts import *

class Player:

    def __init__(self, id, minimax):
        self.id = id
        self.minimax = minimax
        self.mcts = MCTS()

    def movement(self, board):
        if self.id == 1:
            otherPlayerId = 2
        else:
            otherPlayerId = 1
        move = self.mcts.nextMovement(matriz, self, otherPlayerId, False)
        x1 = move['fromX']
        y1 = move['fromY']
        x2 = move['toX']
        y2 = move['toY']

        board[x1][y2] = 0
        board[x2][y2] = self.id 
        
        return board


    def possibleMovements(self, board, otherPlayerId):
        moves = []
        for x in range(0, len(board)):
            for y in range(0, len(board)):
                if (board[x][y] == self.id):
                    for i in range (x - 1, x + 2):
                        for o in range(y - 1, y + 2):
                            if ((i >= 0) and (o >= 0)) and ((i <= 9) and (o <= 9)):
                                try:
                                    value = board[i][o]
                                    if (value == 0):
                                        moves.append({"fromX": x, 
                                                    "fromY": y,
                                                    "toX": i,
                                                    "toY": o,
                                                    "score": 0})
                                    '''if (value == otherPlayerId):
                                        if (board[i][o - 1] == 0) and (o - 1 >= 0): #UP
                                            moves.append({"fromX": x, 
                                                    "fromY": y,
                                                    "toX": i,
                                                    "toY": o - 1,
                                                    "typeOfMove": 1})
                                        elif (board[i][o + 1] == 0) and (o + 1 <= 9): #DOWN
                                            moves.append({"fromX": x, 
                                                    "fromY": y,
                                                    "toX": i,
                                                    "toY": o + 1,
                                                    "typeOfMove": 1})    
                                        elif (board[i - 1][o] == 0) and (i - 1 >= 0): #LEFT
                                            moves.append({"fromX": x, 
                                                    "fromY": y,
                                                    "toX": i - 1,
                                                    "toY": o,
                                                    "typeOfMove": 1})
                                        elif (board[i + 1][o] == 0) and (i + 1 <= 9): #RIGHT
                                            moves.append({"fromX": x, 
                                                    "fromY": y,
                                                    "toX": i + 1,
                                                    "toY": o,
                                                    "typeOfMove": 1})
                                        elif (board[i + 1][o - 1] == 0) and (i + 1 <= 9) and (o - 1 >= 0): #NE
                                            moves.append({"fromX": x, 
                                                    "fromY": y,
                                                    "toX": i + 1,
                                                    "toY": o - 1,
                                                    "typeOfMove": 1})
                                        elif (board[i - 1][o - 1] == 0) and (i - 1 >= 0) and (o - 1 >= 0): #Nw
                                            moves.append({"fromX": x, 
                                                    "fromY": y,
                                                    "toX": i - 1,
                                                    "toY": o - 1,
                                                    "typeOfMove": 1})
                                        elif (board[i + 1][o + 1] == 0) and (i + 1 <= 9) and (o + 1 <= 9): #SE
                                            moves.append({"fromX": x, 
                                                    "fromY": y,
                                                    "toX": i + 1,
                                                    "toY": o + 1,
                                                    "typeOfMove": 1})
                                        elif (board[i - 1][o + 1] == 0) and (i - 1 >= 0) and (o - 1 <= 9): #SW
                                            moves.append({"fromX": x, 
                                                    "fromY": y,
                                                    "toX": i - 1,
                                                    "toY": o + 1,
                                                    "typeOfMove": 1})'''
                                except:
                                    print('Posicion no valida')
        return moves    

    def gameOverCheck(self, board):
        isZero = False

        count1 = 0
        count2 = 0

        counter = 1
        line = ""
        for i in range (len(board) - counter, len(board)):
            for o in range(len(board) - counter, len(board)):
                line = line + str(board[i][o])
                if (board[i][o] == 1):
                    count1 = count1 + 1
                elif (board[i][o] == 2):
                    count2 = count2 + 1
                else:
                    isZero = True
            print(line)
            line = ""
            counter = counter + 1
        if (count1 < count2) and not isZero:
            return True
        else:
            return False       


matriz = [[1,1,1,1,1,0,0,0,0,0],
          [1,1,1,1,0,0,0,0,0,0],
          [1,1,1,0,0,0,0,0,0,0],
          [1,1,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,2],
          [0,0,0,0,0,0,0,0,2,2],
          [0,0,0,0,0,0,0,2,2,2],
          [0,0,0,0,0,0,2,2,2,2],
          [0,0,0,0,0,2,2,2,2,2]]


