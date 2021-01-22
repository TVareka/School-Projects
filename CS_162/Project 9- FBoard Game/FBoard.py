# Author: Ty Vareka
# Date: 3/6/2020
# Description: Made a program to create the game FBoard which is an X vs O game

class FBoard:
    """Creates a class for the FBoard game"""

    def __init__(self):
        self._board = [["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""]]
        self._board[7][7] = "O"
        self._board[5][7] = "O"
        self._board[6][6] = "O"
        self._board[7][5] = "O"
        self._board[0][0] = "X"
        self._XPos = [0, 0]
        self._game_state = "UNFINISHED"

    def get_game_state(self):
        return self._game_state

    def move_x(self, row, column):
        """This function will move the X player to the designated diagonal position"""
        if (self.legal_range(row, column) and (self._game_state == "UNFINISHED") and
                (self._board[row][column] == "") and self.legal_x_move(row, column)):
            self._board[self._XPos[0]][self._XPos[1]] = ""
            self._board[row][column] = "X"
            self._XPos = [row, column]
            if row == 7 and column == 7:
                self._game_state = "X_WON"
            return True
        else:
            return False

    def move_o(self, row_from, column_from, row_to, column_to):
        """This function will move the O piece from a position to another legal position"""
        if ((self.legal_range(row_to, column_to)) and (self._game_state == "UNFINISHED") and
                (self._board[row_to][column_to] == "") and self.legal_o_move(row_from, column_from, row_to, column_to)):
            self._board[row_from][column_from] = ""
            self._board[row_to][column_to] = "O"
            if self.o_win():
                self._game_state = "O_WON"
            return True
        else:
            return False

    def legal_x_move(self, row, column):
        """This function defines what a legal move is for the x player"""
        if ((row + 1 != self._XPos[0] and row - 1 != self._XPos[0]) or
                (column + 1 != self._XPos[1] and column - 1 != self._XPos[1])):
            return False
        else:
            return True

    def legal_o_move(self, row_from, column_from, row_to, column_to):
        """This function defines what a legal move is for the x player"""
        if ((row_from + 1 != row_to and row_from - 1 != row_to) or
                (column_from + 1 != column_to and column_from - 1 != column_to) or
                (row_from + 1 == row_to and column_from + 1 == column_to)):
            return False
        else:
            return True

    def o_win(self):
        """This function determines if o's have surrounded x and leave no legal moves"""
        if (self.x_can_move(self._XPos[0] - 1, self._XPos[1] - 1) or
                self.x_can_move(self._XPos[0] + 1, self._XPos[1] - 1) or
                self.x_can_move(self._XPos[0] - 1, self._XPos[1] + 1) or
                self.x_can_move(self._XPos[0] + 1, self._XPos[1] + 1)):
            return False
        else:
            return True

    def legal_range(self, row, column):
        range = [0, 1, 2, 3, 4, 5, 6, 7]
        if row in range and column in range:
            return True
        else:
            return False

    def x_can_move(self, row, column):
        if (self.legal_range(row, column) and (self._game_state == "UNFINISHED") and
                (self._board[row][column] == "") and self.legal_x_move(row, column)):
            return True
        else:
            return False

    def print_board(self):
        print(self._board)


