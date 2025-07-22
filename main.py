from game_setup import play_game, play_again

if __name__ == "__main__":
    # display game art

    # GAME START
    play_game()

    # WANT TO PLAY AGAIN?
    if play_again():
        play_game()
    else:
        print('Goodbye!')
