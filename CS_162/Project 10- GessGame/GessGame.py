# Author: Ty Vareka
# Date: 5/26/2020
# Description: This project creates a class GessGame that allows the user to play a game called Gess.  All methods
# have docstring descriptors explaining what they do.

class GessGame:
    """Class for the Gess Game"""

    def __init__(self):
        """Must initialize the board and data members. O is white and X is black"""
        self._board = [["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "B", "", "B", "", "B", "B", "B", "B", "B", "B", "B", "B", "", "B", "", "B", "", ""],
                       ["", "B", "B", "B", "", "B", "", "B", "B", "B", "B", "", "B", "", "B", "", "B", "B", "B", ""],
                       ["", "", "B", "", "B", "", "B", "B", "B", "B", "B", "B", "B", "B", "", "B", "", "B", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "B", "", "", "B", "", "", "B", "", "", "B", "", "", "B", "", "", "B", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "W", "", "", "W", "", "", "W", "", "", "W", "", "", "W", "", "", "W", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "W", "", "W", "", "W", "W", "W", "W", "W", "W", "W", "W", "", "W", "", "W", "", ""],
                       ["", "W", "W", "W", "", "W", "", "W", "W", "W", "W", "", "W", "", "W", "", "W", "W", "W", ""],
                       ["", "", "W", "", "W", "", "W", "W", "W", "W", "W", "W", "W", "W", "", "W", "", "W", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]]
        self._game_state = "UNFINISHED"
        self._player_turn = "B"
        self._other_player = "W"
        self._direction = 0
        self._movesteps = 0
        self._ogTile = []
        self._nTile = []

    def get_game_state(self):
        """Takes no parameters and returns the game state"""
        return self._game_state

    def resign_game(self):
        """lets current player concede the game.  Check who's turn it is and changes game state to opposite color
        wins"""
        if self._game_state == "UNFINISHED":
            if self._player_turn == "B":
                self._game_state = "WHITE_WON"
            if self._player_turn == "W":
                self._game_state = "BLACK_WON"

    def make_move(self, curr_pos, new_pos):
        """Checks to make sure the game state is unfinished.  We should then convert the current/new positions to
          a row/column via the index function and make sure that they are on the board.  We next want to check to
          make sure that the current position is a legal tile that is on the board via the legal tile function.
          We then want to check the new position to make sure that it is a legal move via the legal black/white move
          function.  If legal move returns true, it updates the board.  At the end of the turn, if an opponents stone
          is captured, then call the ring on board function to check to see if the game is over."""
        if self._game_state == "UNFINISHED":
            cPos = self.index(curr_pos)
            nPos = self.index(new_pos)
            if not self.legal_range(cPos[0], cPos[1]) or not self.legal_range(nPos[0], nPos[1]):
                return False
            if not self.legal_tile(cPos[0], cPos[1], self._player_turn):
                return False
            if not self.legal_move(cPos[0], cPos[1], nPos[0], nPos[1]):
                return False
            self.move_tile(cPos[0], cPos[1], nPos[0], nPos[1])
            if not self.ring_on_board(self._other_player):
                if self._player_turn == "W":
                    self._game_state = "WHITE_WON"
                else:
                    self._game_state = "BLACK_WON"
                return True
            elif not self.ring_on_board(self._player_turn):
                self.undo_move(cPos[0], cPos[1], nPos[0], nPos[1])
                return False
            else:
                player = self._player_turn
                self._player_turn = self._other_player
                self._other_player = player
                return True
        return False

    def undo_move(self, cRow, cCol, nRow, nCol):
        """Reverts back to original position if your move destroys your own ring"""
        for dc in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                self._board[cRow + dr][cCol + dc] = self._ogTile[dr + 1][dc + 1]
                self._board[nRow + dr][nCol + dc] = self._nTile[dr + 1][dc + 1]
    
    def move_tile(self, cRow, cCol, nRow, nCol):
        """remember layout of tile.  Delete pieces and put tile in the new position"""
        self._ogTile = [[self._board[cRow - 1][cCol - 1], self._board[cRow - 1][cCol], self._board[cRow - 1][cCol + 1]],
                [self._board[cRow][cCol - 1], self._board[cRow][cCol], self._board[cRow][cCol + 1]],
                [self._board[cRow + 1][cCol - 1], self._board[cRow + 1][cCol], self._board[cRow + 1][cCol + 1]]]
        self._nTile = [[self._board[nRow - 1][nCol - 1], self._board[nRow - 1][nCol], self._board[nRow - 1][nCol + 1]],
                        [self._board[nRow][nCol - 1], self._board[nRow][nCol], self._board[nRow][nCol + 1]],
                        [self._board[nRow + 1][nCol - 1], self._board[nRow + 1][nCol], self._board[nRow + 1][nCol + 1]]]
        for dc in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                self._board[cRow + dr][cCol + dc] = ""
        for dc in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                if 0 < nRow + dr < 19 and 0 < nCol + dc < 19:
                    self._board[nRow + dr][nCol + dc] = self._ogTile[dr + 1][dc + 1]

    def legal_move(self, curr_row, curr_col, new_row, new_col):
        """Checks to see if moves are legal for player by checking if number of moves is allowed.  Checks for direction
         of motion is allowed.  Makes sure that the move doesn't cover an opponents piece except on the last step."""
        if not self.check_direction(curr_row, curr_col, new_row, new_col):
            return False
        if self._movesteps > 3 and not self._board[curr_row][curr_col] == self._player_turn:
            return False
        if not self.check_intermediate(curr_row, curr_col):
            return False
        return True

    def check_intermediate(self, cRow, cCol):
        """steps through the moves one at a time and checks to see if the tile is running into opponent's pieces"""

        if self._direction == "EAST":
            cCol += 1
            for i in range(self._movesteps - 1):
                cCol += 1
                if not self.check_empty(cRow-1, cCol) or not self.check_empty(cRow, cCol) or not \
                        self.check_empty(cRow+1, cCol):
                    return False
        elif self._direction == "WEST":
            cCol -= 1
            for i in range(self._movesteps - 1):
                cCol -= 1
                if not self.check_empty(cRow-1, cCol) or not self.check_empty(cRow, cCol) or not \
                        self.check_empty(cRow+1, cCol):
                    return False
        elif self._direction == "NORTH":
            cRow -= 1
            for i in range(self._movesteps - 1):
                cRow -= 1
                if not self.check_empty(cRow, cCol+1) or not self.check_empty(cRow, cCol) or not \
                        self.check_empty(cRow, cCol-1):
                    return False
        elif self._direction == "SOUTH":
            cRow += 1
            for i in range(self._movesteps - 1):
                cRow += 1
                if not self.check_empty(cRow, cCol+1) or not self.check_empty(cRow, cCol) or not \
                        self.check_empty(cRow, cCol-1):
                    return False
        elif self._direction == "NE":
            for i in range(self._movesteps - 1):
                cRow -= 1
                cCol += 1
                if not self.check_empty(cRow-1, cCol-1) or not self.check_empty(cRow-1, cCol) or not \
                        self.check_empty(cRow-1, cCol+1) or not self.check_empty(cRow, cCol+1) or not \
                        self.check_empty(cRow+1, cCol+1):
                    return False
        elif self._direction == "SE":
            for i in range(self._movesteps - 1):
                cRow += 1
                cCol += 1
                if not self.check_empty(cRow - 1, cCol + 1) or not self.check_empty(cRow, cCol+1) or not \
                        self.check_empty(cRow + 1, cCol + 1) or not self.check_empty(cRow+1, cCol) or not \
                        self.check_empty(cRow + 1, cCol - 1):
                    return False
        elif self._direction == "NW":
            for i in range(self._movesteps - 1):
                cRow -= 1
                cCol -= 1
                if not self.check_empty(cRow-1, cCol-1) or not self.check_empty(cRow-1, cCol) or not \
                        self.check_empty(cRow-1, cCol+1) or not self.check_empty(cRow, cCol-1) or not \
                        self.check_empty(cRow+1, cCol-1):
                    return False
        elif self._direction == "SW":
            for i in range(self._movesteps - 1):
                cRow += 1
                cCol -= 1
                if not self.check_empty(cRow - 1, cCol - 1) or not self.check_empty(cRow, cCol-1) or not \
                        self.check_empty(cRow + 1, cCol - 1) or not self.check_empty(cRow+1, cCol) or not \
                        self.check_empty(cRow + 1, cCol + 1):
                    return False
        return True

    def check_empty(self, row, column):
        """Checks to see if location is empty"""

        if self._board[row][column] != "":
            return False
        else:
            return True

    def check_direction(self, cRow, cCol, nRow, nCol):
        """Tells us what direction we are trying to move"""
        if (nRow - cRow) == 0:
            if (nCol - cCol) > 0:
                if self._board[cRow][cCol + 1] == self._player_turn:
                    self._direction = "EAST"
                    self._movesteps = nCol - cCol
                    return True
                else:
                    return False
            else:
                if self._board[cRow][cCol - 1] == self._player_turn:
                    self._direction = "WEST"
                    self._movesteps = cCol - nCol
                    return True
                else:
                    return False
        elif (nCol - cCol) == 0:
            if (nRow - cRow) > 0:
                if self._board[cRow + 1][cCol] == self._player_turn:
                    self._direction = "SOUTH"
                    self._movesteps = nRow - cRow
                    return True
                else:
                    return False
            else:
                if self._board[cRow - 1][cCol] == self._player_turn:
                    self._direction = "NORTH"
                    self._movesteps = cRow - nRow
                    return True
                else:
                    return False
        else:
            rChange = nRow - cRow
            cChange = nCol - cCol
            if rChange == -cChange:
                if rChange > 0:
                    if self._board[cRow + 1][cCol - 1] == self._player_turn:
                        self._direction = "SW"
                        self._movesteps = rChange
                        return True
                    else:
                        return False
                else:
                    if self._board[cRow - 1][cCol + 1] == self._player_turn:
                        self._direction = "NE"
                        self._movesteps = cChange
                        return True
                    else:
                        return False
            elif rChange == cChange:
                if rChange > 0:
                    if self._board[cRow + 1][cCol + 1] == self._player_turn:
                        self._direction = "SE"
                        self._movesteps = rChange
                        return True
                    else:
                        return False
                else:
                    if self._board[cRow - 1][cCol - 1] == self._player_turn:
                        self._direction = "NW"
                        self._movesteps = -cChange
                        return True
                    else:
                        return False
            else:
                return False

    def legal_range(self, row, column):
        """Checks to see if the position is on the board"""
        range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        if row in range and column in range:
            return True
        else:
            return False

    def index(self, position):
        """This function will take a string that the player enters and convert it into an specific location on the
        'board'.  It will return a list with the row/column on the board"""
        if len(position) == 2 or len(position) == 3:
            col = position[0]
            rowstr = position[1:]
            try:
                row = int(rowstr) - 1
            except ValueError:
                return False
            column = str(col).lower()
            column_num = ord(column[0]) - ord('a')
            return [row, column_num]
        else:
            return False

    def legal_tile(self, row, column, player):
        """This function will check to make sure that the tile requested is legal for the player to move.
        It will check the positions surrounding the center point to make sure it only contains player pieces.
        Checks starting tile"""
        pPiece = 0
        for dc in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                piece = self._board[row + dr][column + dc]
                if piece == player:
                    pPiece += 1
                if player == 'B':
                    if piece == 'W':
                        return False
                if player == 'W':
                    if piece == 'B':
                        return False
        if pPiece == 0:
            return False
        return True

    def ring_on_board(self, player):
        """Scans entire board to look for presents of at least one 'ring' for that player.  This is called after every
        move to determine if game is won.  Changes game state if ring cannot be found"""
        for col in range(1, 19):
            for row in range(1, 19):
                if self.tile_is_ring(row, col, player):
                    return True
        return False

    def tile_is_ring(self, row, col, player):
        """Looks at board at that location and determines if that tile is a ring"""
        if self._board[row][col] != "":
            return False
        for dc in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                if dc == 0 and dr == 0:
                    continue
                if self._board[row + dr][col + dc] != player:
                    return False
        return True

    def print_board(self):
        """Prints out the board and also prints all the background variables"""
        for i in range(20):
            print(self._board[i])
        print(self._game_state, self._player_turn, self._other_player, self._direction,self._movesteps)


if __name__ == '__main__':
    game = GessGame()
    #game.print_board()
    #print(game.ring_on_board("W"))
    #print(game.legal_tile(3, 3, "W"))
    #print(game.legal_tile(3, 3, "B"))
    #print(game.index("c5"))
    #print(game.check_direction(6, 5, 3, 2))
    #print(game.check_intermediate(6, 5))
    game.make_move('C6', 'C8')
    game.make_move('R15', 'R12')
    game.make_move('I6', 'I9')
    game.make_move('R18', 'R14')
    game.make_move('I9', 'I11')
    game.make_move('I15', 'I13')
    game.make_move('I3', 'I11')
    game.make_move('F15', 'F14')
    game.make_move('I11', 'Q11')
    game.make_move('R14', 'R13')
    game.make_move('F3', 'J7')
    game.make_move('C18', 'C15')
    game.make_move('J7', 'E12')
    game.make_move('C15', 'B15')
    game.make_move('E12', 'C14')
    game.make_move('R13', 'R12')
    game.make_move('P10', 'Q10')
    game.make_move('R13', 'S12')
    game.make_move('Q9', 'R10')
    game.make_move('S13', 'S12')
    game.make_move('C14', 'E16')
    game.make_move('H18', 'H3')
    game.make_move('L3', 'J3')
    game.make_move('L15', 'L12')
    game.make_move('E16', 'B19')
    game.make_move('O18', 'S14')
    game.make_move('P11', 'P13')
    game.make_move('R14', 'R13')
    game.make_move('J3', 'I3')
    game.make_move('L18', 'L15')
    game.make_move('I3', 'H3')
    game.make_move('L15', 'I12')
    game.make_move('H3', 'H6')
    game.make_move('I12', 'I9')
    game.make_move('H6', 'I7')
    game.print_board()
    """ Test 2
    game.make_move('c3', 'c5')
    game.make_move('c18', 'c16')
    game.make_move('c5', 'd5')
    game.make_move('h14', 'j14')
    game.make_move('d5', 'd6')
    game.make_move('l14', 'h14')
    game.make_move('d6', 'd13')
    game.make_move('g14', 'f14')
    print(game.make_move('j3', 'j6'))
    game.print_board()"""

