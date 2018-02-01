import random

def display_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    shape = ' '
    while not (shape =='x' or shape=='o'):
        shape = input("input X or O").upper()
        if shape == 'X':
            return ('X', 'O')
        else:
            return ('O','X')

def place_shape(board, shape, position):
    board[position]=shape

def win_check(board,shape):
    if((board[1] == shape and board[2] == shape and board[3] == shape) or
      (board[4] == shape and board[5] == shape and board[6] == shape) or
      (board[7] == shape and board[8] == shape and board[9] == shape) or
      (board[1] == shape and board[4] == shape and board[7] == shape) or
      (board[2] == shape and board[5] == shape and board[8] == shape) or
      (board[3] == shape and board[6] == shape and board[9] == shape) or
      (board[1] == shape and board[5] == shape and board[9] == shape) or
      (board[3] == shape and board[5] == shape and board[7] == shape)):
        return True
    else :
        return False

def first_player():
    rand = random.randint (1, 2)
    if rand == 1:
        return 'Player1 turn'
    else:
        return 'Player2 turn'

def space_check(board, position):
    return board[position] ==' '

def full_board_check(board):
    for i in range (1,10):
        if (space_check(board,i)):
            return False
    return True

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        choice = input('Enter position')
        return int (choice)

def replay():
    yn = input('Play Again? Y/N')
    return (yn == 'Y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = first_player()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_shape(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_shape(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break






