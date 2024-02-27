# from IPython.display import clear_output
import random

def display_board(board):
    # clear_output()
    # board = test_board
    # row1 = [board[7], board[8], board[9]]
    # row2 = [board[4], board[5], board[6]]
    # row3 = [board[1], board[2], board[3]]

    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])

    return board


board = [' '] * 10
# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(board)


def player_input():
    '''
    OUTPUT = (Player1 marker, Player2 marker)
    '''

    marker = False
    player_list = ["X", "O"]

    # Choosing who is first
    while marker == False:
        marker = input("Player 1: Do you want to be X or O? ").upper()
        if marker not in player_list:
            print("Sorry, not in X or O")
            marker = False
        else:
            if marker == "X":
                marker = ("X", "O")
                return ('X','O')
                # print(f'player 1 is {marker[0]}')
                # print(f'player 2 is {marker[1]}')

            else:
                marker = ("O","X")
                return ('O', 'X')
                # print(f'player 1 is {marker[0]}')
                # print(f'player 2 is {marker[1]}')


def place_marker(board, marker, position_choice):
    # Choosing the position
    position_choice = False
    acceptable_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    board[position_choice] = marker
    # print(player1)

    while position_choice == False:
        position_choice = input('Please enter a position between 1-9: ')

        if int(position_choice) not in acceptable_values:
            print('Sorry, not in range (1-9)')
            position_choice = False
        else:
            position_choice = int(position_choice)
            print(position_choice)
            board[position_choice] = marker

    display_board(board)

def choose_first():
    if marker == ('X','O'):

        return 'Player 2'
    else:
        return 'Player 1'

player1_marker, player2_marker = player_input()
place_marker(board, "$", 9)

# def win_check(board, mark):
#     if
#
# win_check(board,'X')
