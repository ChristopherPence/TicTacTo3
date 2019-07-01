import sys, json

#Check for a win in the game
#Prints 0 if nobody won
#Prints the code of the player that won
def checkWin():
	#check the 15 seed slots
	#check seeds on the front of cube
	for y in range(0,3):
		for z in range(0,3):
			if(board[0][y][z] > 0):
				checkNeighbors(0,y,z,board[0][y][z])
	
	#check seeds on the left side of cube
	for x in range(1,3):
		for y in range(0,3):
			if(board[x][y][0] > 0):
				checkNeighbors(x,y,0,board[x][y][0])
				
	#check seeds on the top of cube
	for x in range(1,3):
		for z in range(1,3):
			if(board[x][0][z] > 0):
				checkNeighbors(x,0,z,board[x][0][z])

	print("0")

def checkNeighbors(x,y,z,plyr_num):
	#loop through cube around x,y,z
	for a in range(x - 1, x + 2):
		for b in range(y - 1, y + 2):
			for c in range(z - 1, z + 2):
				#check if neighbor == spot
				if(a == x and b == y and c == z):
					continue
				#check if spots are legal
				if(0 <= a <= 2 and 0 <= b <= 2 and 0 <= c <= 2):
					#check if same player in spot
					if(board[a][b][c] == plyr_num):
						checkFinal(x,y,z,a,b,c,plyr_num)

def checkFinal(x,y,z,a,b,c,plyr_num):
	#check the final spot in the line for plyr_num
	# 2nd - 1st = slope
	# slope + 2nd = 3rd
	l = a + (a - x)
	m = b + (b - y)
	n = c + (c - z)
	#verify 3rd slot legal
	if(0 <= l <= 2 and 0 <= m <= 2 and 0 <= n <= 2):
		if(board[l][m][n] == plyr_num):
			#win found
			print(plyr_num)
			sys.exit()

#read the board from nodejs
# f = json.loads(sys.argv[1])
# m = json.loads(sys.argv[2])
# b = json.loads(sys.argv[3])

#set the board for algorithm testing
f = [ [1,0,0], [0,0,0], [0,0,0] ]
m = [ [1,0,0], [0,0,0], [0,0,0] ]
b = [ [2,0,0], [1,0,0], [0,0,0] ]

#convert f,m,b format to board format
board = [f,m,b]

#check for a win and return this to nodejs
win = 0
checkWin()