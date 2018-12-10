import random

TTTBoard = {'1': ' ', '2': ' ', '3': ' ',
			'4': ' ', '5': ' ', '6': ' ',
			'7': ' ', '8': ' ', '9': ' '}

TTTBoardGrid = {'1': '1', '2': '2', '3': '3',
				'4': '4', '5': '5', '6': '6',
				'7': '7', '8': '8', '9': '9'}

def printBoard(board):
	print("\n=================")
	print("     |     |     ")
	print("  {}  |  {}  |  {}  ".format(board['1'], board['2'], board['3']))
	print("     |     |     ")
	print("-----+-----+-----")
	print("     |     |     ")
	print("  {}  |  {}  |  {}  ".format(board['4'], board['5'], board['6']))
	print("     |     |     ")
	print("-----+-----+-----")
	print("     |     |     ")
	print("  {}  |  {}  |  {}  ".format(board['7'], board['8'], board['9']))
	print("     |     |     ")
	print("=================\n")

printBoard(TTTBoardGrid)
print("Welcome to a command-line Tic-Tac-Toe!\n")

turns = 0
allowedSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def checkWin(board, symbol, player):
	win = 1
	if TTTBoard['1'] == symbol and TTTBoard['2'] == symbol and TTTBoard['3'] == symbol:
		print(player + " won!")
		return win
	if TTTBoard['4'] == symbol and TTTBoard['5'] == symbol and TTTBoard['6'] == symbol:
		print(player + " won!")
		return win
	if TTTBoard['7'] == symbol and TTTBoard['8'] == symbol and TTTBoard['9'] == symbol:
		print(player + " won!")
		return win
	if TTTBoard['1'] == symbol and TTTBoard['4'] == symbol and TTTBoard['7'] == symbol:
		print(player + " won!")
		return win
	if TTTBoard['2'] == symbol and TTTBoard['5'] == symbol and TTTBoard['8'] == symbol:
		print(player + " won!")
		return win
	if TTTBoard['3'] == symbol and TTTBoard['6'] == symbol and TTTBoard['9'] == symbol:
		print(player + " won!")
		return win
	if TTTBoard['1'] == symbol and TTTBoard['5'] == symbol and TTTBoard['9'] == symbol:
		print(player + " won!")
		return win
	if TTTBoard['3'] == symbol and TTTBoard['5'] == symbol and TTTBoard['7'] == symbol:
		print(player + " won!")
		return win

while True:
	move = str(input("It's your turn. What space do you want to fill? (Type quit to exit): "))
	if move.lower() == 'quit':
		break
	TTTBoard[move] = 'x'
	allowedSpaces.remove(int(move))
	turns += 1
	printBoard(TTTBoard)
	if turns == 9:
		break
	win = checkWin(TTTBoard, 'x', 'You')
	if win == 1:
		break

	print("-----------------")
	print("v v  AI Turn  v v")
	print("-----------------")

	aiMove = str(random.choice(allowedSpaces))
	TTTBoard[aiMove] = 'o'
	allowedSpaces.remove(int(aiMove))
	turns += 1
	printBoard(TTTBoard)
	win = checkWin(TTTBoard, 'o', 'The AI')
	if win == 1:
		break