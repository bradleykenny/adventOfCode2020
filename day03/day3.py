import math

print("========== PART 1 ==========")

inFile = open("day3.txt")

arr = [line.replace("\n", "") for line in inFile]
n = len(arr)

posX = 0
treesEnc = 0
for line in arr:
    finalPos = posX % len(line)
    if (line[finalPos] == "#"):
        treesEnc += 1
    posX += 3
print(treesEnc)


print("\n========== PART 2 ==========")

total = 1
combs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for comb in combs:
    posX = 0
    i = 0
    treesEnc = 0
    while i < n:
        finalPos = posX % len(arr[i])
        if (arr[i][finalPos] == "#"):
            treesEnc += 1
        posX += comb[0]
        i += comb[1]
    total *= treesEnc
print(total)
