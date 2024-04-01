class AIPlayer:
    def __init__(self):
        self.root = None
        self.b = None
        self.MAX_DEPTH = 5

    def return_best_move(self):
        MAX = float("-inf")
        best_move = None

        # Iterate through available moves from the root node and select the move with the highest score
        for move, child_node in self.root.children.items():
            if child_node.score > MAX:
                MAX = child_node.score
                best_move = move

        return best_move