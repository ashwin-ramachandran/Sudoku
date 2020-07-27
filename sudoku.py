# A sample board (all boards must be 2D lists)
board = [
	[7,8,0,4,0,0,1,2,0],
	[6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,2,6,0],
	[0,0,1,0,5,0,9,3,0],
	[9,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[0,4,9,2,0,6,0,0,7]
]

# Function to print the board, so user may see a before and after being solved
def print_board(board):
	# Access the outer elements indexes
	for i in range(len(board)):
		# Print a horizontal divider line after every third row
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - -")
		# Access the inner elements indexes
		for j in range(len(board[i])):
			# Print a vertical divider line after every third column
			if j % 3 == 0 and j != 0:
				print(" | ", end = "")

			# Specific conditional formatting to make the board print out symmetric and in a visually appealing manner
			if j == 8:
				print(board[i][j])
			else:
				if j == 0:
					print(" " + str(board[i][j]) + " ", end = "")
				elif j == 2 or j == 5:
					print(str(board[i][j]), end = "")
				else:
					print(str(board[i][j]) + " ", end = "")

# Function for locating an empty spot on the board (indicated by a value of 0), returning that location in a (row, col) fashion
def find_empty_spot(board):
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 0:
				return (i, j) # (row, col)
	# Returns None if there are no more empty spots (in other words, the board is solved)
	return None

# Function for checking if the attempted entry is valid (if it will work according to the rules of Sudoku)
def valid(board, num, pos):
	# Check the row to see if the number entered already exists in that row
	for i in range(len(board[0])):
		if board[pos[0]][i] == num and pos[1] != i:
			return False

	# Check the column to see if the number entered already exists in that column
	for i in range(len(board)):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	# Check the spot's local 3x3 box to see if the number entered already exists in that box

	# x and y coordinates of the spot's position relative to its local 3x3 box
	box_x = pos[1] // 3
	box_y = pos[0] // 3

	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x*3, box_x*3 + 3):
			if board[i][j] == num and (i, j) != pos:
				return False

	# True will only be returned if all the checks have been passed, that is if the attempted entry does not exist in the spot's row, column, or local box
	return True

# Recursive function that implements the other functions as well to actually do the solving of the board
def solve(board):
	# Find an empty spot on the board and return its position to the find variable
	find = find_empty_spot(board)

	# Base case
	# Will only execute and return True if find holds the value of None, which will only happen if no empty spots exist (meaning the board has been solved already)
	if not find:
		return True

	# Recursive case
	else:
		row, col = find

	# Loop will cause i to hold the values of 1-9, the only legal entries in a Sudoku board
	for i in range(1, 10):
		# Check if entering the value that i holds (some int 1-9) into the board in the specified (row, col) position is valid
		if valid(board, i, (row, col)):
			# If it is valid, then make the entry
			board[row][col] = i

			# Enter another function call
			if solve(board):
				return True

			# If solve(board) returns False, the board spot must be reset to 0 (this is where the backtracking comes into play)
			board[row][col] = 0

	return False

print_board(board)
solve(board)
print_board(board)
