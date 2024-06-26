import math

class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.visits = 0
        self.score = 0
        self.children = {}
        self.parent = parent

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

    def expand_node(self, node):
        # Expand the given node by adding children representing possible moves
        available_points = self.b.get_available_points()
        for point in available_points:
            # Create a new child node for each available point
            new_state = self.b.copy_state()
            new_state.place_a_move(point, 1)  # Assuming it's AI's turn
            node.children[point] = TreeNode(new_state, node)

    def rollout(self, node):
        # Perform a fixed-depth minimax search for rollout from the given node
        depth = 1
        alpha = float("-inf")
        beta = float("inf")
        return self.minimax(depth, 2, node.state, alpha, beta)  # Assuming it's opponent's turn

    def update_tree(self, move):
        # Update the tree structure based on the move chosen in the rollout
        if move in self.root.children:
            self.root = self.root.children[move]
            self.root.parent = None  # Reset the parent of the new root node
        else:
            # If the move is not in the tree, create a new node for it
            new_state = self.b.copy_state()
            new_state.place_a_move(move, 1)  # Assuming it's AI's turn
            self.root = TreeNode(new_state)
            self.root.visits = 1

    def select_best_child(self, node):
        # Select the child with the highest UCB score
        best_child = None
        best_score = float("-inf")
        for child in node.children.values():
            score = self.calculate_ucb_score(child)
            if score > best_score:
                best_score = score
                best_child = child
        return best_child

    def calculate_ucb_score(self, node):
        # Calculate the UCB score for a given node
        exploration_factor = 1.4  # Tunable parameter
        exploitation_term = node.score / node.visits if node.visits > 0 else 0
        exploration_term = exploration_factor * (math.sqrt(math.log(node.parent.visits) / node.visits))
        return exploitation_term + exploration_term

    def perform_mcts(self, b):
        self.b = b
        if self.root is None:
            # Initialise the root node with the current game state
            self.root = TreeNode(b.copy_state())

        # Perform MCTS with Minimax Rollouts
        for _ in range(1000):  # Perform 1000 iterations (can be adjusted)
            selected_node = self.select_node_to_expand(self.root)
            self.expand_node(selected_node)
            rollout_node = self.select_best_child(selected_node)
            rollout_result = self.rollout(rollout_node)
            self.backpropagate(rollout_node, rollout_result)

        # Select the best move based on the UCB scores of the root's children
        best_move = self.return_best_move()
        # Update the tree structure based on the chosen move
        self.update_tree(best_move)
        return best_move

    def backpropagate(self, node, score):
        # Backpropagate the rollout result up the tree
        while node is not None:
            node.visits += 1
            node.score += score
            node = node.parent

    def select_node_to_expand(self, node):
        # Traverse the tree to select a node for expansion
        while len(node.children) > 0:
            if node.visits == 0:
                return node
            else:
                node = self.select_best_child(node)
        return node

    def minimax(self, depth, turn, state, alpha, beta):
        # Base case: Check if the game has ended or if maximum depth is reached
        if state.is_game_over() or depth == self.MAX_DEPTH:
            # Evaluate the state and return its score
            if state.has_x_won():
                return 1
            elif state.has_o_won():
                return -1
            else:
                return 0

        # If it's AI's turn (MAX player)
        if turn == 1:
            max_score = float("-inf")
            # Iterate over possible moves
            for move in state.possible_moves():
                # Make the move
                state.place_a_move(move, turn)
                # Recursively call minimax to find the best move
                score = self.minimax(depth + 1, 2, state, alpha, beta)
                # Undo the move
                state.undo_last_move(move)
                # Update alpha
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break  # Beta cut-off
            return max_score
        else:
            min_score = float("inf")
            # Iterate over possible moves
            for move in state.possible_moves():
                # Make the move
                state.place_a_move(move, turn)
                # Recursively call minimax to find the best move
                score = self.minimax(depth + 1, 1, state, alpha, beta)
                # Undo the move
                state.undo_last_move(move)
                # Update beta
                min_score = min(min_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break  # Alpha cut-off
            return min_score
