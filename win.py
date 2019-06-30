import sys, json

print("Game Start")

#Check for a win in the game
#Returns 0 if nobody wins
#Returns the player code upon win condition
def checkWin():
	#check the 15 seed slots
	#check seeds in f dimension
	for y in range(0,3):
		for z in range(0,3):
			if(board[0][y][z] > 0):
				print("slot (0,%1d,%1d) = %1d" %(y,z,board[0][y][z]))

	#check seeds in m dimension
	for y in range(0,3):
		if(board[1][y][0] > 0):
			print("slot (1,%1d,0) = %1d" %(y,board[1][y][0]))

	#check seeds in b dimension
	for y in range(0,3):
		if(board[2][y][0] > 0):
			print("slot (2,%1d,0) = %1d" %(y,board[2][y][0]))


def checkNeighbors(plyr_num):
	#load actual neighbors of 14 possible into queue
	print("TODO")
	#check immediate neighbors

	#if one of those is the same number, check the final slot



#read the board from nodejs
# f = json.loads(sys.argv[1])
# m = json.loads(sys.argv[2])
# b = json.loads(sys.argv[3])

#set the board for algorithm testing
f = [ [0,0,0], [1,0,0], [0,0,0] ]
m = [ [2,0,0], [0,0,0], [0,0,2] ]
b = [ [0,3,0], [0,0,0], [3,0,0] ]

#convert f,m,b format to board format
board = [f,m,b]

print(board[0][1][0])
print(board[1][2][2])
print(board[2][0][1])

#check for a win and return this to nodejs
checkWin()

