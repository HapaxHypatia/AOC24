sampleData = [
'MMMSXXMASM',
'MSAMXMSMSA',
'AMXSXMAAMM',
'MSAMASMSMX',
'XMASAMXAMM',
'XXAMMXXAMA',
'SMSMSASXSS',
'SAXAMASAAA',
'MAMMMXMMMM',
'MXMXAXMASX'
]

with open("04.txt", 'r') as file:
	data = [x.strip() for x in file.readlines()]

# data = sampleData


def check(x, y, xRange, yRange):
	try:
		coords = [(y+eval(yRange), x+eval(xRange)) for i in range(4)]
		for tup in coords:
			if tup[0] < 0 or tup[1] < 0:
				return False
		string = "".join([data[y+eval(yRange)][x+eval(xRange)] for i in range(4)])
		if string == "XMAS":
			return coords
		else:
			return False
	except IndexError:
		return False


def duplicate_check(matchList):
	sortedMatches = [sorted(m) for m in matchList]
	return len(set(tuple(i) for i in sortedMatches))


moves = ["i", "0", "-i"]

matchesA = []

for y in range(len(data)):						# row
	for x in range(len(data[y])):					# character
		for item1 in moves:							# ranges for y
			for item2 in moves:						# ranges for x
				match = check(x, y, item1, item2)
				if match:
					matchesA.append(match)


print("a = ", str(duplicate_check(matchesA)))


def checkB(x, y):
	try:
		a = ((y - 1, x - 1), (y, x), (y + 1, x + 1))
		b = ((y + 1, x + 1), (y, x), (y - 1, x - 1))
		c = ((y - 1, x + 1), (y, x), (y + 1, x - 1))
		d = ((y + 1, x - 1), (y, x), (y - 1, x + 1))
		patterns = [a, b, c, d]
		matches = 0
		for p in patterns:
			for tup in p:
				if tup[0] < 0 or tup[1] < 0:
					return False
			if "".join([data[tup[0]][tup[1]] for tup in p]) == "MAS":
				matches += 1
		if matches == 2:
			return True
	except IndexError:
		return False


matchesB = []
for y in range(len(data)):								# row
	for x in range(len(data[y])):						# character
		if data[y][x] == "A":
			if checkB(x, y):
				matchesB.append((x, y))

# print("b = ", str(duplicate_check(matchesB)))
print("b = ", str(len(matchesB)))
