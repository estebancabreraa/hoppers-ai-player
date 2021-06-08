import random

class MCTS:

    def __init__(self):
        self.algo = 'mcts'

    def nextMovement(self, board, player, otherPlayerId, sim):
        if not sim:
            moves = player.possibleMovements(board, otherPlayerId)

            #leer score

            bestMoves = []

            score = 0

            for move in moves:
                currentScore = move['score']

                if currentScore >= score:
                    score = currentScore
                    bestMoves.append(move)
                else:
                    continue

            moveIndex = random.randint(1, len(bestMoves)) - 1
            return bestMoves[moveIndex] 
        #simulation






            
        

