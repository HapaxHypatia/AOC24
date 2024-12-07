sampleRules = [
	(47, 53),
	(97, 13),
	(97, 61),
	(97, 47),
	(75, 29),
	(61, 13),
	(75, 53),
	(29, 13),
	(97, 29),
	(53, 29),
	(61, 53),
	(97, 53),
	(61, 29),
	(47, 13),
	(75, 47),
	(97, 75),
	(47, 61),
	(75, 61),
	(47, 29),
	(75, 13),
	(53, 13),
]

sampleUpdates = [
	[75, 47, 61, 53, 29],
	[97, 61, 53, 29, 13],
	[75, 29, 13],
	[75, 97, 47, 61, 53],
	[61, 13, 29],
	[97, 13, 75, 29, 47],
]

with open("05 rules.txt", 'r') as file:
	data = [x.strip().split("|") for x in file.readlines()]
	rules = [[int(y) for y in x] for x in data]
with open("05 pages.txt", 'r') as file:
	data = [x.strip().split(",") for x in file.readlines()]
	updates = [[int(y) for y in x] for x in data]

# rules, updates = sampleRules, sampleUpdates

fixed = []


def checkUpdate(u):
	for r in rules:
		if r[0] in u and r[1] in u:
			if u.index(r[0]) > u.index(r[1]):
				u[u.index(r[0])], u[u.index(r[1])] = r[1], r[0]
				fixed.append(u)
				return False
	middle = int(len(u)/2 + 0.5)-1
	return u[middle]


result = sum(checkUpdate(u) for u in updates)
print(result)

fixedResult = sum(checkUpdate(u) for u in fixed)
print(fixedResult)
