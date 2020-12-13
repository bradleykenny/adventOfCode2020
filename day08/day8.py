import copy

print("========== PART 1 ==========")

inFile = open("day8.txt")

arr = [line.replace("\n", "") for line in inFile]
arr = [line.split(" ") for line in arr]

# acc = increases accumulator
# jmp = jumps to new instruction relative to itself (e.g. jmp +2 skips 1 instruction)
# nop = does nothing and goes to next line

i = 0
acc = 0
visited = []

while i < len(arr):
	if i in visited:
		break
	else:
		visited.append(i)
	if arr[i][0] == "acc":
		acc += int(arr[i][1])
		i += 1
	elif arr[i][0] == "jmp":
		i += int(arr[i][1])
	elif arr[i][0] == "nop":
		i += 1
print(acc)
	

print("\n========== PART 2 ==========")

for visit in visited:
	i = 0
	acc = 0
	newVisits = []
	temp = copy.deepcopy(arr)
	if temp[visit][0] == "jmp":
		temp[visit][0] = "nop"
	elif temp[visit][0] == "nop":
		temp[visit][0] = "jmp"
	
	while i < len(temp):
		if i in newVisits:
			i = 0
			break
		else:
			newVisits.append(i)
		if temp[i][0] == "acc":
			acc += int(temp[i][1])
			i += 1
		elif temp[i][0] == "jmp":
			i += int(temp[i][1])
		elif temp[i][0] == "nop":
			i += 1
	if i >= len(temp):
		print(acc)