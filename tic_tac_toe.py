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
    ok = False
    while not ok:
        try:
            turn = int(input("Where do you wanna play: "))
            if turn < 1 or turn > 9:
                raise ValueError("Out of range, please enter a number between 1 and 9.")
            turn -= 1  # cell's number from 0 to 8
            row = turn // 3  # cell's row
            col = turn % 3  # cell's column
            if board[row][col] in ['O', 'X']:
                raise ValueError("That spot is already occupied, please select a different spot.")
            ok = True
        except ValueError as e:
            print(e)#if not i is inputed
    board[row][col] = 'O'  # set '0' at the selected square

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
    if sign not in ["X", "O"]:
        return None
    who = "me" if sign == "X" else "you"
    #uses the all() function with a generator expression to check if all
    # the elements in a row or column are equal to the given sign.

    # check rows
    for row in range(3):
        if all(board[row][col] == sign for col in range(3)):
            return who

    # check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return who

    # check diagonals
    if all(board[i][i] == sign for i in range(3)):
        return who
    if all(board[i][2-i] == sign for i in range(3)):
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
human_turn = True # which turn is it now?
while len(free):
	DisplayBoard(board)
	if human_turn:
		enter_move(board)
		victor = VictoryFor(board,'O')
	else:
		DrawMove(board)
		victor = VictoryFor(board,'X')
	if victor != None:
		break
	human_turn = not human_turn
	free = (board)

DisplayBoard(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")
