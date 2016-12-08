"""
A system for learning the optimal strategies for winning othello.
"""

class Othello(object):

    ROWS = 8
    COLUMNS = 8
    EMPTY = 0
    WHITE = 1
    BLACK = 2

    def __init__(self):
        self.currentTurn = 'white'
        self.board = self.blankBoard()
        self.initialBoard()


    def __str__(self):
        return "\n".join(["{}".format(row) for row in self.board])


    def blankBoard(self):
        """
        Generate an 8x8 (ROWS by COLUMNS) board with two white squares and two black squares
        :return:
        """
        board = [[self.EMPTY for c in range(self.COLUMNS)] for r in range(self.ROWS)]
        return board


    def initialBoard(self):
        self.placeToken(self.WHITE, 3, 3)
        self.placeToken(self.BLACK, 3, 4)
        self.placeToken(self.WHITE, 4, 4)
        self.placeToken(self.BLACK, 4, 3)
        return


    def placeToken(self, value, x_coord, y_coord):
        self.board[y_coord][x_coord] = value
        return


    def generateBoard():
        pass




if __name__ == '__main__':
    print "Let's learn how to play {}".format("othello.")
    o = Othello()
    print o
