"""
A system for learning the optimal strategies for winning othello.

"""

class Othello(object):

    ROWS = 8
    COLUMNS = 8
    EMPTY = '_'
    WHITE = 'W'
    BLACK = 'B'

    def __init__(self):
        self.currentTurn = self.WHITE
        self.board = self.blankBoard()
        self.initial_board()



    def __str__(self):
        return "\n".join(["{}".format(row) for row in self.board])


    def blankBoard(self):
        """
        Generate an 8x8 (ROWS by COLUMNS) board with two white squares and two black squares
        :return:
        """
        board = [[self.EMPTY for c in range(self.COLUMNS)] for r in range(self.ROWS)]
        return board


    def initial_board(self):
        self.place_token(self.WHITE, 3, 3)
        self.place_token(self.BLACK, 3, 4)
        self.place_token(self.WHITE, 4, 4)
        self.place_token(self.BLACK, 4, 3)
        return


    def place_token(self, value, x_coord, y_coord):
        self.board[y_coord][x_coord] = value
        return


    def identify_potential_moves(self):
        """Returns a list of coordinates where the current player could place a token."""
        potential_moves = set([])
        opponent_cells = self.find_opponent_cells()
        for ox, oy in opponent_cells:
            adj_oc = self.get_adjacent_cells(ox, oy)
            for ax, ay in adj_oc:
                # TODO: Add check to calculate that placing a token in this spot would flank an opponent token.
                potential_moves.add((ax,ay))
        return potential_moves

    def mark_cells(self, cells_of_interest):
        for cx, cy in cells_of_interest:
            self.place_token('P', cx, cy)
        return


    def find_opponent_cells(self):
        # Find opponent spaces
        if self.currentTurn == self.WHITE:
            opponent = self.BLACK
        else:
            opponent = self.WHITE
        opponent_cells = []
        for x_coord, row in enumerate(self.board):
            for y_coord, space in enumerate(row):
                if space == opponent:
                    opponent_cells.append((x_coord, y_coord))

        print opponent_cells
        return opponent_cells


    def get_adjacent_cells(self, x_coord, y_coord):
        """Returns empty cells adjacent to given coordinates"""
        coord_transforms = [(-1, -1), (0, -1), (1, -1),
                          (-1, 0), (1, 0),
                          (-1, 1), (0, 1), (1,1)]
        adjacent_cells = []
        for xt, yt in coord_transforms:
            ax = x_coord + xt
            ay = y_coord + yt
            if ax >= 0 and ay >=0 and self.board[ax][ay] == self.EMPTY:
                adjacent_cells.append((ax,ay))
        print adjacent_cells
        return adjacent_cells

    def take_turn(self):
        p = self.identify_potential_moves()
        self.mark_cells(p)
        return

    def get_direction(self, coordinate_a, coordinate_b):
        ax, ay = coordinate_a
        bx, by = coordinate_b
        cx = bx - ax
        cy = by - ay
        direction = 'invalid'
        if cx == 1:
            if cy == 0:
                direction = 'east'
            elif cy == 1:
                direction = 'south-east'
            elif cy == -1:
                direction = 'north-east'
        elif cx == 0:
            if cy == 1:
                direction = 'south'
            elif cy == -1:
                direction = 'north'
        elif cx == -1:
            if cy == 1:
                direction = 'south-west'
            elif cy == 0:
                direction = 'west'
            elif cy == -1:
                direction = 'north-west'
        if direction == 'invalid':
            print "Warning 001: invalid direction. Possibly bad coordinate set: [{}, {}]".format(coordinate_a, coordinate_b)
        return direction


    def get_vector(self, direction):
        """takes a direction and returns a tuple which can be used for vector addition in order to move from a
        given point in a given direction"""
        direction_vectors = {
            'east': (1,0),
            'south-east': (1,1),
            'north-east': (1,-1),
            'south': (0,1),
            'north': (0,-1),
            'south-west': (-1,1),
            'west': (-1,0),
            'north-west': (-1,-1)
        }
        # This will throw a KeyError exception direction is not one of the dictionary keys.
        return direction_vectors['direction']

    def score_potential_move(self, coordinates, opponent):
        x_coord, y_coord = coordinates
        adjacent_cells = self.get_adjacent_cells(x_coord, y_coord)
        total_score = 0
        target_tokens = set()

        for ax, ay in adjacent_cells:
            # Find an opponent cell in an adjacent cell.
            if self.board[ax, ay] == opponent:
                direction =
                # Determine how many opponent tokens would be flipped

        # Repeat until all opponent cells have been examined.
        # Do not double count cells.



if __name__ == '__main__':
    print "Let's learn how to play {}".format("othello.")
    o = Othello()
    print o
    o.take_turn()
    print o