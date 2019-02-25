### Abdul Kasim, Jan 2018
### Main Body
import connectfour
import time
from collections import namedtuple

BOARD_COLUMNS = 7
BOARD_ROWS = 6
GameState = namedtuple('GameState', ['board', 'turn'])
empty_board = GameState(board=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], turn=1)
game_state = empty_board
def run_user_interface()->None:
    print('Welcome to the Connect Four Ultimate Gaming Experience!')
    print(" a. New game \n b. Exit")
    while True:
        command = input("Please enter a command: ")
        if command == 'a':
            pick_color()
            break
        if command == 'b':
            print("*********************************************")
            print('Thanks for playing! Have a nice day!')
            break
        else:
            print('Error')

def pick_color():
    print('*****************************************************************')
    print('Optimizing game board...')
    print('*****************************************************************')
    time.sleep(.5)
    print_board(empty_board)
    while True:
        command = input('Player 1, which color you want to be?\na. Red \nb. Yellow \nplease pick your color: ')
        if command == 'a':
            print('Player1 : Red \nPlayer2 : Yellow \nRed goes first')
            a = make_move(empty_board)
            if a == "Red":
                print("Red won!")
                break
            if a == "Yellow":
                print("Yellow won!")
                break
        if command == 'b':
            print('Player1 : Yellow \nPlayer2 : Red \nRed goes first')
            a = make_move(empty_board)
            if a == "Red":
                print("Red won!")
                break
            if a == "Yellow":
                print("Yellow won!")
                break
        else:
            print('Error')


def make_move(game_state: GameState):
    print()
    while True:
        if connectfour_import.winner(game_state) == 1:
            return "Red"
        if connectfour_import.winner(game_state) == 2:
            return "Yellow"
        print(user_turn(game_state), "'s turn")
        command = input('What do you want to do? \n a.Drop \n b.Pop\nPlease indicate your move (a or b): ')
        if command == 'a':
            new_game_state = drop_command(game_state)
            print_board(new_game_state)
            return make_move(new_game_state)
        if command == 'b':
            new_game_state = pop_command(game_state)
            print_board(new_game_state)
            return make_move(new_game_state)
        else:
            print('error')

   
        
    
### private functions
def print_board(game_state: GameState)->None:
    print("1 2 3 4 5 6 7")
    for row in range(BOARD_ROWS):
        row_str = ''
        for col in range(BOARD_COLUMNS):
            if game_state.board[col][row] == 0:
                row_str += '.'+' '
            if game_state.board[col][row] == 1:
                row_str += 'R'+' '
            if game_state.board[col][row] == 2:
                row_str += 'Y'+' '
        print(row_str)




    
def user_turn(game_state: GameState):
    if game_state.turn == 1:
        return 'Red'
    if game_state.turn % 2 == 1:
        return 'Red'
    if game_state.turn % 2 == 0:
        return 'Yellow'
        





def drop_command(game_state: GameState):
    while True:
        column_num = input('Please enter the column number that you wish to drop your piece: ')
        try:
            column_num=int(column_num)
            return connectfour_import.drop(game_state, column_num-1)
        except:
            print( "Error: Please enter a valid column number (only integers between 0 and 7)!")


   


def pop_command(game_state: GameState):
    while True:
        column_num = input('Please enter the column number that you wish to pop your piece: ')
        try:
            column_num=int(column_num)
            return connectfour_import.pop(game_state, column_num-1)
        except:
            print( "Error: Please enter a valid column number (only integers between 0 and 7)!")


    
    



run_user_interface()
