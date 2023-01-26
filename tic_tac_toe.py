from random import randrange

def DisplayBoard(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
	print("+-------" * 3,"+",sep="")
	for row in range(3):
		print("|       " * 3,"|",sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ",end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their turn,
    # checks the input, and updates the board according to the user's decision.
	ok = False	# fake assumption - we need it to enter the loop
	while not ok:
		turn = int(input("Where do you wanna play: "))
		ok = turn >= 1 and turn <= 9 # is user's input valid?
		if not ok:
			print("Out of range retry!") # no, it isn't - do the input again
			continue
		turn = turn - 1 	# cell's number from 0 to 8
		row = turn // 3 	# cell's row
		col = turn % 3		# cell's column
		position = board[row][col]	# check the selected square
		ok = position not in ['O','X']
		if not ok:	# it's occupied - to the input again
			print("Occupied!..Please retry your input!")
			continue
	board[row][col] = 'O' 	# set '0' at the selected square

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
	free = []	#empty list declaration
    #iteration through row and column
	for row in range(3):
		for col in range(3):
			if board[row][col] not in ['O','X']:
				free.append((row,col)) #append new tuple to the list
	return free


def VictoryFor(board,sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
	if sign == "X":
		who = 'me'	# Computer's side
	elif sign == "O":
		who = 'you'	# Your side
	else:
		who = None
	cross1 = cross2 = True
	for rc in range(3):
		if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
			return who
		if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
			return who
		if board[rc][rc] != sign:
			cross1 = False
		if board[2 - rc][2 - rc] != sign:
			cross2 = False
	if cross1 or cross2:
		return who
	return None

def DrawMove(board):
    # The function draws the computer's move and updates the board.
	free = make_list_of_free_fields(board)
	cnt = len(free)
	if cnt > 0:
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # make an empty board
board[1][1] = 'X' # set first 'X' in the middle
free = make_list_of_free_fields(board)
humanturn = True # which turn is it now?
while len(free):
	DisplayBoard(board)
	if humanturn:
		enter_move(board)
		victor = VictoryFor(board,'O')
	else:
		DrawMove(board)
		victor = VictoryFor(board,'X')
	if victor != None:
		break
	humanturn = not humanturn
	free = (board)

DisplayBoard(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")
