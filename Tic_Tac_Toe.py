#Jayden Williams
#Tic Tac Toe
#11/11/19

#

# Global Constants
X = "X"
O = "O"
EMPTY = " "
NUM_SQUARES = 9


#working
def intro():
    """ display game instructions """
    print("""
     _____ _        _____            _____          
|_   _(_)      |_   _|          |_   _|         
  | |  _  ___    | | __ _  ___    | | ___   ___ 
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \
  | | | | (__    | | (_| | (__    | | (_) |  __/
  \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|
                                                
                                                
    
    Enter a number 1-9. The number will correspond to the board position as illustrated:
                
                1 | 2 | 3
                ---------
                4 | 5 | 6
                ---------
                7 | 8 | 9
    """)


def new_board():
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Display game board on screen"""
    print(str.format("""
                {0} | {1} | {2}
                ---------
                {3} | {4} | {5}
                ---------
                {6} | {7} | {8}
                """,board[0],board[1],board[2],
                     board[3],board[4],board[5],
                     board[6],board[7],board[8]))

#board = new_board()
#print(board)
#display_board(board)
#board[0] = X
#display_board(board)
#board[4] = 0
#display_board(board)

#working
def ask_yes_no(question):
    """Ask a yes or no question. and give a one letter response back"""
    response = None
    while response not in ("y","n","yes","no"):
        response = input(question).lower()
    x = response[0]
    return x

def ask_number(question, low, high):
    response = None
    while response not in range(low,high):
        try:
            response = int(input(question))
        except:
            print("not a number")

    return response

