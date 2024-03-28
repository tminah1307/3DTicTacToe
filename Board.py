class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "[" + str(self.x + 1) + ", " + str(self.y + 1) + ", " + str(self.z + 1) + "]"

class PointsAndScores:
    def __init__ (self, score, point):
        self.score = score
        self.point = point

class Board:
    def __init__ (self):
        self.available_points = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
        self.board = [[[0 for i in range(3)]for i in range(3)]for i in range(3)]
    
    def is_game_over(self):
        return (self.has_x_won() or self.has_o_won() or len(self.get_available_points()) == 0)
    
    def has_x_won(self):
        return self.check_winning_conditions(1)


    def has_o_won(self):
        return self.check_winning_conditions(2)
    
    def check_winning_conditions(self, player):
        # check rows, columns, and layers
        for i in range(3):
            if any(self.check_line(self.board[i][j], player) for j in range(3)) or \
            any(self.check_line(self.board[i][j], player) for j in range(3)) or \
            any(self.check_line([self.board[k][j][i] for k in range(3)], player) for j in range(3)):
                return True
        
        # check diagonals across layers
        if any(self.check_line([self.board[k][i][j] for k in range(3)], player) for j in range(3)) or \
        any(self.check_line([self.board[k][i][2-j] for k in range(3)], player) for j in range(3)):
            return True
        return False
        
    # Get available points on the board
    def get_available_points(self):
        available_points = []
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.board[x][y][z] == 0:
                        available_points.append((x, y, z))
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
                for cell in row:
                    if cell == 1:
                        print("X", end=" ")
                    elif cell == 2:
                        print("O", end=" ")
                    else:
                        print(".", end=" ")
                print()
            print()
