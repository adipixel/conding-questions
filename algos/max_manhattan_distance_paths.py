def getMaxManhattanDistancePaths(x, y):
	mat = [[0 for _ in range(y)] for _ in range(x)]
	# initialization
	print(mat)
	for i in range(x):
		mat[i][0] = 1
	for i in range(y):
		mat[0][i] = 1

	for i in range(1, x):
		for j in range(1, y):
			mat[i][j] = max( [mat[i][j-1], mat[i-1][j]]   ) + 1

	return mat[x-1][y-1]

def main():
	x1, y1 = 0, 0
	x2, y2 = 4, 4
	xnew, ynew = abs(x2-x1)+1, abs(y2-y1)+1

	print (getMaxManhattanDistancePaths(xnew, ynew))

main()
