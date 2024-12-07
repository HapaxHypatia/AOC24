import re


def calculate_result(matchlist):
	pattern2 = r"\d+"
	return sum([int(re.findall(pattern2, m)[0]) * int(re.findall(pattern2, m)[1]) for m in matchlist])



with open("03.txt", 'r') as file:
	data = file.read()

# data = sampleData = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


pattern1 = r"mul\(\d+,\d+\)"
matches = re.findall(pattern1, data)
print(calculate_result(matches))

muls = list(re.finditer(pattern1, data))
dos = []
donts = []

for ind in range(len(data)):
	if data[ind: ind + 4] == "do()":
		dos.append(ind)
	elif data[ind: ind + 7] == "don't()":
		donts.append(ind)

matchList = []
do = True
for ind in range(len(data)):
	if ind in donts:
		do = False
		# print("not doing...")
	if ind in dos:
		do = True
		# print("doing...")
	if do:
		if ind in [m.start() for m in muls]:
			m = list(filter(lambda x: x.start() == ind, muls))
			matchList.append(m[0].group())
			# print(m[0].group())

print(calculate_result(matchList))

