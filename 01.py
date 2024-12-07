# Sample data
# list1 = [3,4,2,1,3,3]
# list2 = [4,3,5,3,9,3]

with open("01.txt", 'r') as file:
	data = [x.split() for x in file.readlines()]
	list1 = sorted([int(line[0]) for line in data])
	list2 = sorted([int(line[1]) for line in data])

result1 = sum(max(list1[i], list2[i]) - min(list1[i], list2[i]) for i in range(len(list1)))
print(result1)

result2 = sum(a * sum(1 for b in list2 if b == a) for a in list1)
print(result2)
