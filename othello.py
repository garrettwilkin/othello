"""
A system for learning the optimal strategies for winning othello.
"""

class Othello(object):

    ROWS = 8
    COLUMNS = 8

    def __init__(self):
        self.currentTurn = 'white'
        self.board = self.intialBoard


    def __str__(self):
        return "\n".join(["{}".format(row) for row in self.board()])

    def intialBoard(self):
        """
        Generate an 8x8 (ROWS by COLUMNS) board with two white squares and two black squares
        :return:
        """
        board = [[0 for c in range(self.COLUMNS)] for r in range(self.ROWS)]
        return board

    def generateBoard():
        pass




if __name__ == '__main__':
    print "Let's learn how to play {}".format("othello.")
    o = Othello()
    print o
