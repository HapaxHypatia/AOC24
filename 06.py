with open("06.txt", 'r') as file:
	data = [x.strip() for x in file.readlines()]

sampledata = [
	'....#.....',
	'.........#',
	'..........',
	'..#.......',
	'.......#..',
	'..........',
	'.#..^.....',
	'........#.',
	'#.........',
	'......#...',
]

data = sampledata

loopObstacles = [
	(3, 6), (6, 7), (3, 8), (1, 8), (7, 7), (7, 9)
]


def create_squares():
	squares = []
	for y in range(len(data)):
		for x in range(len(data[y])):
			value = data[y][x]
			squares.append(
				{
					'x': x,
					'y': y,
					'value': value
				})
	return squares


def reset():
	global tracker
	tracker = []
	squares = create_squares()
	return squares


def isLoop(indices):
	# square has been repeated at least 3 times
	global tracker
	looptestA = tracker[indices[1]:indices[2]]
	looptestB = tracker[indices[2]:indices[3]]
	if looptestA == looptestB:
		return True
	else:
		looptestA = tracker[indices[1]:indices[3]]
		looptestB = tracker[indices[3]:indices[5]]
		if looptestA == looptestB:
			return True
		else:
			print("No repeating substring found")
			return False


def move_guard(square):
	print(square['x'], square['y'])
	global tracker

	# check direction
	match square["value"]:
		case "^":
			coords = square['x'], square['y'] - 1
			nextdir = ">"
		case ">":
			coords = square['x'] + 1, square['y']
			nextdir = "v"
		case "v":
			coords = square['x'], square['y'] + 1
			nextdir = "<"
		case "<":
			coords = square['x'] - 1, square['y']
			nextdir = "^"

	# check square in front
	nextSquare = list(filter(lambda sq: sq["x"] == coords[0] and sq['y'] == coords[1], squares))
	if len(nextSquare) < 1:
		square['value'] = 'X'
		return False
	else:
		nextSquare = nextSquare[0]

	# if empty, move 1 square
	global obstacles, testObstacle
	if nextSquare['value'] in ".X":
		if nextSquare['value'] == "X":
			try:
				indices = [ind for ind, item in enumerate(tracker) if item[0] == nextSquare['x'] and item[1] == nextSquare['y']]
				if len(indices) > 6:
					# check the tracker for a repeating sequence
					if isLoop(indices):
						obstacles.append(testObstacle)
						print(f"Loop created with obstacle placed at {testObstacle}")
						return False
					else:
						if (testObstacle['x'], testObstacle['y']) in loopObstacles:
							print("Loop not identified")
							return False
			except NameError:
				pass
		nextSquare['value'] = square['value']
		square['value'] = 'X'
		tracker.append((square['x'], square['y']))
		# print(f"Guard at x: {nextSquare['x']}, y: {nextSquare['y']}")
		return True
	# else turn right
	else:
		square['value'] = nextdir
		# print(f"Guard at x: {square['x']}, y: {square['y']}")
		return True


squares = create_squares()
empty = list(filter(lambda sq: sq["value"] == '.', squares))
testObstacle = None
obstacles = []

for item in empty:
	tracker = []
	squares = create_squares()
	testObstacle = list(filter(lambda sq: sq["x"] == item["x"] and sq["y"] == item["y"], squares))[0]
	print('\n\n\n\n\n Testing obstacle at:', testObstacle['x'], testObstacle['y'])

	location = squares.index(testObstacle)
	squares[location]['value'] = '#'
	# find guard
	isGuard = True
	while isGuard:
		try:
			guardLocation = list(filter(lambda sq: sq["value"] in ['^', '>', 'v', '<'], squares))[0]
			if not move_guard(guardLocation):
				isGuard = False
				print(f"Obstacle locations found: {obstacles}")
		except IndexError:
			isGuard = False
print(f"Number of obstacles found: {len(obstacles)}")
# Part 1
# visited = len(list(filter(lambda sq: sq["value"] == "X", squares)))
# print(visited)




