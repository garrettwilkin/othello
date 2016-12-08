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

if __name__ == '__main__':
    print "Let's learn how to play {}".format("othello.")
    o = Othello()
    print o
    o.take_turn()
    print o