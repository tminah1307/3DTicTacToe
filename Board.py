# Class Point represents a point in a 3D space.
class Point:
    # Initialises a point with given x, y, z coordinates
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # Returns a string representation of the point
    def __str__(self):
        return "[" + str(self.x + 1) + ", " + str(self.y + 1) + ", " + str(self.z + 1) + "]"

# Class represents a combination of score and associated point on the board
class PointsAndScores:
    def __init__ (self, score, point):
        self.score = score
        self.point = point

# Class Board represent the game board (state space) for 3D Tic Tac Toe
class Board:
    def __init__ (self):
        self.available_points = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
        self.board = [[[0 for i in range(3)]for i in range(3)]for i in range(3)]

    # Checks if the game has ended
    def is_game_over(self):
        return (self.has_x_won() or self.has_o_won() or len(self.get_available_points()) == 0)
    
    # Checks if player X has won 
    def has_x_won(self):
        return self.check_winning_conditions(1)

    # Checks if player O has won 
    def has_o_won(self):
        return self.check_winning_conditions(2)
    
    # Check x, y, z coordinates for each row to validate a win
    def check_winning_conditions(self, player):

        # Check rows, columns, and layers 
        # Iterate through each index for each dimension
        for i in range(3):
            if any(self.check_line(self.board[i][j], player) for i in range(3)) or \
            any(self.check_line(self.board[i][j], player) for j in range(3)) or \
            any(self.check_line([self.board[k][j][i] for k in range(3)], player) for j in range(3)):
                return True
        
        # Check diagonals across layers
        # Iterate through each diagonal dimension
        if any(self.check_line([self.board[k][i][j] for k in range(3)], player) for j in range(3)) or \
        any(self.check_line([self.board[k][i][2-j] for k in range(3)], player) for j in range(3)):
            return True
        return False
        
    # Get available points on the board
    def get_available_points(self):
        available_points = [(x, y, z) for x in range(3) for y in range(3) for z in range(3) if self.board[x][y][z] == 0]
        return available_points

    # Get state of a specific point on the board
    def get_state(self, point):
        x, y, z = point
        return self.board[x][y][z]

    # Place a move on the board
    def place_a_move(self, point, player):
        x, y, z = point
        self.board[x][y][z] = player

    # Display the current state of the board
    def display_board(self):
        print()
        for layer in self.board:
            for row in layer:
                print(" ".join(["X" if cell == 1 else "O" if cell == 2 else "." for cell in row]))
            print()
