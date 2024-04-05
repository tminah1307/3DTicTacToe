class TreeNode:
    def __init__(self, state):
        self.state = state
        self.visits = 0
        self.score = 0
        self.children = {}