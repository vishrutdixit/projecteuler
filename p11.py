# coding=utf-8
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

with open("p011_grid.txt") as matrix:
	lines = [line.split(' ') for line in matrix]

# converting strings to ints
	for i in range(0, len(lines)):
		for j in range(0, len(lines[i])):
			lines[i][j] = int(lines[i][j])

max_res = 0

for x in range(0, len(lines)):
	for y in range(0, len(lines[x])):

		horizontal = 1
		vertical = 1
		diagonal_right = 1
		diagonal_left = 1

		for i in range(0, 4):
			if(y+i < 20):
				horizontal *= lines[x][y+i]
			if (x+i < 20):
				vertical *= lines[x+i][y]
			if (x+i < 20 and y+i < 20):
				diagonal_right *= lines[x+i][y+i]
			if (x+i < 20 and y-i >= 0):
				diagonal_left *= lines[x+i][y-i]

		max_res = max(max_res, horizontal, vertical, diagonal_left, diagonal_right)

print max_res
