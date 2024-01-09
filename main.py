# tic tac toe game

import random
import time

# global variables
board = [' ' for x in range(10)]
player = 'X'
computer = 'O'
winner = None
turn = 'X'


# print board
def print_board():
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


# check if board is full
def is_board_full():
    if board.count(' ') > 1:
        return False
    else:
        return True


# check if there is a winner
def check_winner():
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# check rows
def check_rows():
    global game_still_going
    row_1 = board[1] == board[2] == board[3] != ' '
    row_2 = board[4] == board[5] == board[6] != ' '
    row_3 = board[7] == board[8] == board[9] != ' '
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[1]
    elif row_2:
        return board[4]
    elif row_3:
        return board[7]


# check columns
def check_columns():
    global game_still_going
    column_1 = board[1] == board[4] == board[7] != ' '
    column_2 = board[2] == board[5] == board[8] != ' '
    column_3 = board[3] == board[6] == board[9] != ' '
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[1]
    elif column_2:
        return board[2]
    elif column_3:
        return board[3]


# check diagonals
def check_diagonals():
    global game_still_going
    diagonal_1 = board[1] == board[5] == board[9] != ' '
    diagonal_2 = board[3] == board[5] == board[7] != ' '
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[1]
    elif diagonal_2:
        return board[3]


# flip player
def flip_player():
    global turn
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'


# check if game is over
def check_game_over():
    check_winner()
    check_tie()


# check if there is a tie
def check_tie():
    global game_still_going
    if is_board_full() and winner is None:
        game_still_going = False


# get computer move
def get_computer_move():
    global board
    # check if computer can win
    for i in range(1, 10):
        if board[i] == ' ':
            board[i] = computer
            if check_winner() is not None:
                return i
            else:
                board[i] = ' '
    # check if player can win
    for i in range(1, 10):
        if board[i] == ' ':
            board[i] = player
            if check_winner() is not None:
                board[i] = computer
                return i
            else:
                board[i] = ' '
    # check if center is free
    if board[5] == ' ':
        return 5
    # check if corner is free
    corners_open = []
    for i in [1, 3, 7, 9]:
        if board[i] == ' ':
            corners_open.append(i)
    if len(corners_open) > 0:
        return random.choice(corners_open)
    # check if side is free
    sides_open = []
    for i in [2, 4, 6, 8]:
        if board[i] == ' ':
            sides_open.append(i)
    if len(sides_open) > 0:
        return random.choice(sides_open)


# play game
def play_game():
    global winner
    print_board()
    while not is_board_full() and winner is None:
        if turn == 'X':
            player_move()
            print_board()
            check_game_over()
            flip_player()
        else:
            computer_move()
            print_board()
            check_game_over()
            flip_player()

        check_rows()
        check_columns()
        check_diagonals()

    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner is None:
        print('Tie.')


# player move
def player_move():
    print('Your turn.')
    move = input('Enter position (1-9): ')
    valid = False
    while not valid:
        while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            move = input('Enter position (1-9): ')
        move = int(move)
        if board[move] == ' ':
            valid = True
        else:
            print('Position already taken.')
    board[move] = player


# computer move
def computer_move():
    print('Computer\'s turn.')
    time.sleep(1)
    move = get_computer_move()
    board[move] = computer


# play again
def play_again():
    global board, winner, turn, game_still_going
    board = [' ' for x in range(10)]
    winner = None
    turn = 'X'
    game_still_going = True
    play_game()


# main
def main():
    play_game()
    while input('Play again? (y/n): ').lower() == 'y':
        play_again()
    print('Bye.')


# run main
if __name__ == '__main__':
    main()

# end of file
