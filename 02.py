# data = [
# 	[7, 6, 4, 2, 1],
# 	[1, 2, 7, 8, 9],
# 	[9, 7, 6, 2, 1],
# 	[1, 3, 2, 4, 5],
# 	[8, 6, 4, 4, 1],
# 	[1, 3, 6, 7, 9],
# 	]


def is_safe(report):
	if report[0] == report[1]:
		return False
	direction = 'increase' if report[1] > report[0] else 'decrease'
	for ind in range(len(report)-1):
		if direction == "increase":
			if report[ind + 1] - report[ind] not in [1, 2, 3]:
				return False
		elif report[ind] - report[ind + 1] not in [1, 2, 3]:
			return False
	return True

with open("02.txt", 'r') as file:
	data = [x.strip().split() for x in file.readlines()]

print(sum(1 for x in data if is_safe([int(y) for y in x])))

safe = 0
for x in data:
	report = [int(y) for y in x]
	if is_safe(report):
		safe += 1
	else:
		for ind in range(len(report)):
			new_report = [report[i] for i in range(len(report)) if i != ind]
			if is_safe(new_report):
				safe += 1
				break

print(safe)

