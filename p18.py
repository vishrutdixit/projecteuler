'''
pyramid maximum path sum

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

def solve(lines, bottom):
	# base case
	if(bottom == -1):
		return lines[0][0]
	# recurse, collapsing pyramid
	for i in range(0, len(lines[bottom])):
		lines[bottom][i] = max(lines[bottom][i]+lines[bottom+1][i], lines[bottom][i]+lines[bottom+1][i+1])
	return solve(lines, bottom-1)


def main(filename):
	with open(filename) as matrix:
		lines = [line.split(' ') for line in matrix]

	# converting strings to ints
	for i in range(0, len(lines)):
		for j in range(0, len(lines[i])):
			lines[i][j] = int(lines[i][j])

	return solve(lines, len(lines)-2)

if __name__ == "__main__":
	print main("p018_triangle.txt")



