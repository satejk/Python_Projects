
# Author : SATEJ V. KHANDEPARKAR
# Masters in embedded and intelligent systems from
# Halmstad university ,sweden.

# BATTLESHIP_2.0 is developed for bigger board and longer battleship
from random import randint

board = []   # declare a empty list

board_size = raw_input("Enter the size of the board (greater than 8):") # set the size of board

for x in range(int(board_size)):
    board.append(["O"] * int(board_size))   # initialize with "O" to form a 5 x 5 matrix

def print_board(board):
    for row in board:
        print " ".join(row)   # print the board without [] and ''
print "*********************"
print "Let's play Battleship!"
print "*********************"

print "The Battleship is 3 boxes wide"
print "******************************"

print_board(board)	      # print the initialized board		

def random_row(board):
    return randint(0, len(board) - 4)  # returns a random row number since the ship is 3 boxes wide
    								   # randomness must be limited to accomodate it on the board.

def random_col(board):
    return randint(0, len(board) - 4)  # returns a random coloumn number

ship_row = random_row(board)    # store the row number    
ship_col = random_col(board)	#store the column number

print ship_row         # uncomment only for debugging       
print ship_col		# uncomment only for debugging	

# gaming for loop starts

for turn in range(8):
    
    guess_row = int(raw_input("Guess Row:"))    # row input from user 
    guess_col = int(raw_input("Guess Col:"))	# column input from user

    if (guess_row == ship_row) and ((guess_col == ship_col) or (guess_col == ship_col + 1 ) or (guess_col == ship_col + 2 )):   # for inputs that are a hit
        print "You hit my battleship!"
        board[guess_row][guess_col] = "B"
        print_board(board) 
        print "Turn", turn + 1
        if (turn == 7):
        	print "Game Over"
        else:
        	pass
        if(board[ship_row][ship_col] == "B" and board[ship_row][ship_col + 1] == "B" and board[ship_row][ship_col + 2] == "B"):
        	print "YOU SUNK MY BATTLESHIP .....CONGRATS"
        	print "**********GAME OVER*****************"
        	break
        
        
               	
        		
        	
    else:
        if (guess_row < 0 or guess_row > (len(board) - 1)) or (guess_col < 0 or guess_col > (len(board)-1)):
            print "Oops, that's not even in the ocean."     # for inputs outside the board
            print "Turn", turn + 1
            print_board(board)
            if (turn == 7):
                print "Game Over"
                
        elif(board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "B" ):    # for inputs that have already been guessed
            print "You guessed that one already."
            print "Turn", turn + 1
            print_board(board)
            if (turn == 7):
                print "Game Over"
                
        else:
            print "You missed my battleship!"         # for inputs that are a miss
            board[guess_row][guess_col] = "X"
            print "Turn", turn + 1
            print_board(board)
            
            if (turn == 7):
                print "Game Over"
                
#############################################################################################3                
                
                
                
