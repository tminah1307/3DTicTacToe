from itertools import product

class GameState:
    EMPTY_BOARD = ' ' # Empty cell
    BOARD_SIZE = 3 

    # Initialise a game state
    def __init__(self, board=None, current_player='X'):
        if board is None:
            self.board = [[self.EMPTY_BOARD] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        else:
            self.board = board
        self.current_player = current_player

    # Clone the current game state for move exploration
    def clone(self):
        cloned_board = [[[cell for cell in row] for row in layer] for layer in self.board]
        return GameState(cloned_board, self.current_player)

    # Get the current player
    def get_current_player(self):
        return self.current_player

    # String representation of the game state
    def __str__(self):
        board_str = "\n".join(["\n".join(["|".join(row) for row in layer]) for layer in self.board])
        separator = "\n" + "--" * self.BOARD_SIZE + "\n" # Separators between layers
        # Segment the string and join with separators
        return separator.join([board_str[i:i+self.BOARD_SIZE*2-1] for i in range(0, len(board_str), self.BOARD_SIZE*2-1)])

    # Check if the game has been won using check_line
    def is_goal(self):
        # Define directions to check for winning lines
        directions = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1), (-1, 1, 1)]
        for i, j, k in product(range(self.BOARD_SIZE), repeat=3):
            for dx, dy, dz in directions:
                if self.check_line(i, j, k, dx, dy, dz):
                    return True # Winning line found
        return False # No winning line found

    # Check for winning line starting from a given cell in a given direction
    def check_line(self, x, y, z, dx, dy, dz):
        first_cell = self.board[x][y][z] # Get the symbol of the first cell in the line
        if first_cell == self.EMPTY_BOARD: # If the cell is empty, there is no winning line
            return False
        # Iterate over each subsequent cell in the line
        for i in range(1, self.BOARD_SIZE):
            new_x, new_y, new_z = x + i * dx, y + i * dy, z + i * dz
            # Check if the next cell is within the bounds of the board and contains the same symbol
            if not (0 <= new_x < self.BOARD_SIZE and 0 <= new_y < self.BOARD_SIZE and 0 <= new_z < self.BOARD_SIZE and 
                    self.board[new_x][new_y][new_z] == first_cell):
                return i >= self.BOARD_SIZE - 1 # Return True if a winning line is formed
        return True

    # Check if there are any empty cells left on the board iteratively
    def check_draw(self):
        return not any(self.EMPTY_BOARD in row for layer in self.board for row in layer)

    # Generate possible moves for the current player
    def possible_moves(self):
        moves = [] # Initialize a list to store possible moves
        # Iterate over each cell in the board
        for i, j, k in product(range(self.BOARD_SIZE), repeat=3):
            # If the cell is empty, create a new game state with the move and add it to the list of moves
            if self.board[i][j][k] == self.EMPTY_BOARD:
                new_board = [[[cell for cell in row] for row in layer] for layer in self.board]
                new_board[i][j][k] = self.current_player
                next_player = 'O' if self.current_player == 'X' else 'X' # Switch the player
                moves.append(GameState(new_board, next_player)) # Add the new game state to the list of moves
        return moves # Return the list of possible moves
