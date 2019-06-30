import sys, json

print("Game Start");

# f = json.loads(sys.argv[1])
# m = json.loads(sys.argv[2])
# b = json.loads(sys.argv[3])

f = [ [0,0,0], [1,0,0], [0,0,0] ]
m = [ [0,0,0], [0,0,0], [0,0,2] ]
b = [ [0,3,0], [0,0,0], [0,0,0] ]

print(f[1][0])
print(m[2][2])
print(b[0][1])

def checkWin():
	