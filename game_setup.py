from tic_tac_toe import *
from game_art import ttt_art
import time 

def play_game():
    """TIC TAC TOE GAME"""
    global players_turn, game_on
    game_on = True

    print(ttt_art)
    
    print("Welcome to TIC - TAC - TOE !!!")
    chosen_role = input("Please choose your character (e.g., 'X' or 'O'): ")
    game = TicTacToe(character=chosen_role)

    print(f"\nHere is a list of available in-game moves:\n{game.board_moves}\n")

    if game.player == 'X':
        players_turn = True

    while game_on:
        game.display_board()

        if game.is_winner():
            if game.player == game.is_winner():
                print("Player Wins")
            else:
                print("Computer Wins... Ha Ha Ha.. erm Ha!")

            game_on = False
            
        else:
            if players_turn:
                print("\nPlayer's turn...!!!\n")
                move = input('Please make a move (e.g., top left, center right, etc.): ').upper()
                game.make_move(move=move, character=game.player)
                players_turn = False
            else:
                print("\nComputer is Process... One Moment!\n")
                time.sleep(1)
                move = game.get_computer_move()
                game.make_move(move=move, character=game.computer)
                players_turn = True

        if game.is_draw():
            print("GAME - DRAW!!")
            game_on = False

def play_again():
    """Checks if the Player wants to continue playing the game."""
    play_again = input('Would you like to play another game [ yes | no ]: ').lower()
    if play_again.startswith('y'):
        return True
    return False