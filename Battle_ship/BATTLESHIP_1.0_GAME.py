
# Author : SATEJ V. KHANDEPARKAR
# Masters in embedded and intelligent systems from
# Halmstad university ,sweden.


from random import randint

board = []   # declare a empty list

for x in range(5):
    board.append(["O"] * 5)   # initialize with "O" to form a 5 x 5 matrix

def print_board(board):
    for row in board:
        print " ".join(row)   # print the board without [] and ''

print "Let's play Battleship!"
print_board(board)	      # print the initialized board		

def random_row(board):
    return randint(0, len(board) - 1)  # returns a random row number

def random_col(board):
    return randint(0, len(board[0]) - 1)  # returns a random coloumn number

ship_row = random_row(board)    # store the row number    
ship_col = random_col(board)	#store the column number

#print ship_row         # uncomment only for debugging       
#print ship_col		# uncomment only for debugging	

# gaming for loop starts

for turn in range(4):
    
    guess_row = int(raw_input("Guess Row:"))    # row input from user 
    guess_col = int(raw_input("Guess Col:"))	# column input from user

    if (guess_row == ship_row) and (guess_col == ship_col):   # for inputs that are a hit
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col] = "B"
        print_board(board) 
        print "Turn", turn + 1
        print "Game Over"
        break  # exit game
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."     # for inputs outside the board
            print "Turn", turn + 1
            
            if (turn == 3):
                print "Game Over"
                
        elif(board[guess_row][guess_col] == "X"):    # for inputs that have already been guessed
            print "You guessed that one already."
            print "Turn", turn + 1
            
            if (turn == 3):
                print "Game Over"
                
        else:
            print "You missed my battleship!"         # for inputs that are a miss
            board[guess_row][guess_col] = "X"
            print "Turn", turn + 1
            print_board(board)
            
            if (turn == 3):
                print "Game Over"
                
#############################################################################################3                
                
                
                
