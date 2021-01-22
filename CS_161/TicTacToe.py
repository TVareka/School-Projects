# Author: Ty Vareka
# Date: 2/25/2020
# Description: Create a game of tictactoe using a 3x3 board that changes states when you draw or win

class TicTacToe:
    """Creates a tictactoe class which allows you to play tictactoe"""
    def __init__(self):
        self._board = [["", "", ""],
                       ["", "", ""],
                       ["", "", ""]]
        self._current_state = "UNFINISHED"
        self._turn = 0

    def make_move(self, row, column, player):
        """This function decides when a user has played a legal move and will change the current state to draw
        if the board is full."""
        range = [0, 1, 2]
        if ((self._current_state == "UNFINISHED") and (row in range) and (column in range) and
                (self._board[column][row] == "")):
            self._turn += 1
            if player == "x" or player == "X":
                self._board[column][row] = "X"
            else:
                self._board[column][row] = "O"
            self.did_win(self._board[column][row])
            if self._turn == 9 and self._current_state == "UNFINISHED":
                self._current_state = "DRAW"
            return True
        else:
            return False

    def get_current_state(self):
        return self._current_state

    def did_win(self, le):
        """This function determines if a player has one the game by having three x's or o's in a row on the board"""
        if ((self._board[0][0] == le and self._board[0][1] == le and self._board[0][2] == le) or
           (self._board[1][0] == le and self._board[1][1] == le and self._board[1][2] == le) or
           (self._board[2][0] == le and self._board[2][1] == le and self._board[2][2] == le) or
           (self._board[0][0] == le and self._board[1][0] == le and self._board[2][0] == le) or
           (self._board[0][1] == le and self._board[1][1] == le and self._board[2][1] == le) or
           (self._board[0][2] == le and self._board[1][2] == le and self._board[2][2] == le) or
           (self._board[0][0] == le and self._board[1][1] == le and self._board[2][2] == le) or
           (self._board[0][2] == le and self._board[1][1] == le and self._board[2][0] == le)):
            if le == "X":
                self._current_state = "X_WON"
            else:
                self._current_state = "O_WON"











