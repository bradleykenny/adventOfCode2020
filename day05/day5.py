print("========== PART 1 ==========")

inFile = open("day5.txt")

arr = [line.replace("\n", "") for line in inFile]
n = len(arr)

highest = 0
ids = {}

for line in arr:
    seat = [char for char in line]
    lower = 0
    upper = 127
    for i in range(0, 7):
        # lower half
        if seat[i] == "F":
            upper = (upper / 2) + (lower / 2)
        # upper half
        elif seat[i] == "B":
            lower = (lower / 2) + (upper / 2) + 1

    left = 0
    right = 7
    for i in range(7, 10):
        if seat[i] == "L":
            right = (right / 2) + (left / 2)
        elif seat[i] == "R":
            left = (left / 2) + (right / 2) + 1

    id = left + upper * 8
    if highest < id:
        highest = id
    ids[str(id)] = [left, upper]

print(highest)

print("\n========== PART 2 ==========")

allIDs = {}
for i in range(0, highest):
    allIDs[str(i)] = False

for id in ids:
    allIDs[id] = True

for id in allIDs:
    if allIDs[id] != True and int(id) > 8:
        print(str(id))
