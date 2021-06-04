class Player:

    def __init__(self, id, minimax):
        self.id = id
        self.minimax = minimax

    def movement(self):
        i = 10 #later

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
                                                    "typeOfMove": 0})
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

#def eval(self, board):




'''matriz = [[1,1,1,1,1,0,0,0,0,0],
          [1,1,1,1,0,2,0,0,0,0],
          [1,1,1,0,0,0,0,0,0,0],
          [1,1,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,2],
          [0,0,0,0,0,0,0,0,2,2],
          [0,0,0,0,0,0,0,2,2,2],
          [0,0,0,0,0,0,2,2,2,2],
          [0,0,0,0,0,2,2,2,2,2]]

player1 = Player(1, True)

for move in player1.possibleMovements(matriz, 2):
    print(move)'''

