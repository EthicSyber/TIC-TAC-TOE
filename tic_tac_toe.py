import random

# GAME FLAGS
game_on = False
players_turn = False

# GAME MOVES
TOP = 'TOP'
TOP_LEFT = 'TOP LEFT'
TOP_RIGHT = 'TOP RIGHT'
CENTER = 'CENTER'
CENTER_LEFT = 'CENTER LEFT'
CENTER_RIGHT = 'CENTER RIGHT'
BOTTOM = 'BOTTOM'
BOTTOM_LEFT = 'BOTTOM LEFT'
BOTTOM_RIGHT = 'BOTTOM RIGHT'


# GAME OBJECT
class TicTacToe:
    """The Classic Tic-Tac-Toe Game"""
    def __init__(self, character:str):
        self.board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
        self.board_coordinates = {TOP_LEFT:(0,0), TOP:(0,1), TOP_RIGHT: (0, 2), CENTER_LEFT: (1,0), CENTER: (1,1), CENTER_RIGHT:(1,2), BOTTOM_LEFT:(2,0),BOTTOM:(2,1),BOTTOM_RIGHT:(2,2)}
        self.board_moves = [key for key in self.board_coordinates]
        self.player, self.computer = self.choose_character(character)
    
    def display_board(self):
        """Displays the game board for the current game"""
        print('\n' * 100)
        print('---+---+---')
        for row in self.board:
            print(f" {row[0]} | {row[1]} | {row[2]} ")
            print('---+---+---')

    def choose_character(self, character:str) -> tuple[str, str]:
        """Allows the Player to choose a character for the game. 'X' | 'Y'"""

        if character.upper() == 'X':
            player, computer = ['X', 'O']
        else:
            player, computer = ['O', 'X']

        return player, computer

    def make_move(self, move:str, character:str) -> None:
        """Places a X or O on the board for a player | computer move
        
        :params str move: the move key for board coordinates (e.g., Player chooses 'TOP LEFT')
        :params str character: the 'X' or 'O' that was chosen at the beginning of the game
        """
        if move in self.board_moves:
            y, x = self.board_coordinates[move]
            self.board[y][x] = character
        

    def get_available_moves(self) -> list:
        """Checks if there are available moves on the board
        
        :returns available_moves: a list of tuples as available coordinates from the board

        Example:
        >>> [(0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        """

        available_moves = []
        # unavailable_moves = []

        for y in range(3):
            row = self.board[y]
            for x in range(3):
                if row[x] == '*':
                    available_moves.append((y, x))
                else:
                    continue
                    # unavailable_moves.append((y, x))

        return available_moves
    
    def get_unavailable_moves(self) -> list:
        unavailable_moves = []
        for y in range(3):
            row = self.board[y]
            for x in range(3):
                if row[x] != '*':
                    unavailable_moves.append((y, x))
                else:
                    continue
        return unavailable_moves

    def check_move_close(self):
        """Checks if there is a closer move available to potentially block the player"""
        for a_move in self.get_available_moves():
            for u_move in self.get_unavailable_moves():
                u_x_plus, u_x_minus = u_move[1]+1, u_move[1]-1
                if u_move[0] == a_move[0] and (u_x_plus == a_move[1] or u_x_minus == a_move[1]):
                    return a_move
                # else:
                #     return False
        return False
            
    def get_computer_move(self):
        """Gets a move for the computer to make
        
        :returns key: key of the available move on the game board
        """
        a_move = random.choice(self.get_available_moves())
        close_move = self.check_move_close()
        for key, val in self.board_coordinates.items():
            if close_move == val:
                return key
            else:
                if val == a_move:
                    return key
        return key
                
    def get_grid_items(self) -> list:
        """Checks sequence of board for X or O character. 
    
        :returns list: a list of every sequence from the tick tac toe board
        """
        rows_and_columns = []
        diag_lines = [self.board[0][0], self.board[1][1], self.board[2][2]], [self.board[0][2], self.board[1][1], self.board[2][0]]
        columns = [list(item) for item in zip(*iter(self.board))]

        for row in self.board:
            rows_and_columns.append(row)
        for diag in diag_lines:
            rows_and_columns.append(diag)
        for col in columns:
            rows_and_columns.append(col)

        return rows_and_columns

    def is_winner(self):
        """Checks the winner of the Game
        
        :returns winner: if the winner is found (otherwise, False)
        """
        rows_and_columns = self.get_grid_items()
        for item in rows_and_columns:
            if "*" in item:
                continue
            else:
                check = item[0] == item[1] == item[2]
                if check:
                    winner = item[0]
                    return winner
        return False
    
    def is_draw(self) -> bool:
        """Checks if game is a draw"""
        if self.get_available_moves() == []:
            return True
        else:
            return False
        

        





