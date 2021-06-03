class Game:

    def __init__(self, players):
        self.players = players
        self.board = [[1,1,1,1,1,0,0,0,0,0],
                    [1,1,1,1,0,2,0,0,0,0],
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

    def progress(self):
        while not self.over:
            i = 10

    

    