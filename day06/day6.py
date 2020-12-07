import copy

print("========== PART 1 ==========")

inFile = open("day6.txt")

arr = [line.replace("\n", "") for line in inFile]
arr.append('')

total = 0
yesAns = []
for item in arr:
    if item == '':
        total += len(yesAns)
        yesAns = []
    else:
        chars = [char for char in item]
        for char in chars:
            if char not in yesAns:
                yesAns.append(char)

print(total)


print("\n========== PART 2 ==========")

total = 0
yesAnsTemp = {}
tempChar = chr(ord('a'))
while tempChar <= 'z':
    yesAnsTemp[tempChar] = 0
    tempChar = chr(ord(tempChar) + 1)

yesAns = copy.deepcopy(yesAnsTemp)
numPeople = 0

for item in arr:
    if item == '':
        for key in yesAns:
            if yesAns[key] == numPeople:
                total += 1
        yesAns = copy.deepcopy(yesAnsTemp)
        numPeople = 0
    else:
        chars = [char for char in item]
        for char in chars:
            yesAns[char] += 1
        numPeople += 1
print(total)
