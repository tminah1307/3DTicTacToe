class AIPlayer:
    def __init__(self):
        self.root = None
        self.b = None
        self.MAX_DEPTH = 5

    def return_best_move(self):
        MAX = float("-inf")
        best_move = None