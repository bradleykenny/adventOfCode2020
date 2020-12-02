import math

print("========== PART 1 ==========")

inFile = open("day2.txt")

arr = [line.replace("\n", "").split(" ") for line in inFile]
count = 0
for pwd in arr:
    lower = int(pwd[0].split("-")[0])
    upper = int(pwd[0].split("-")[1])
    char = pwd[1][0]
    if pwd[2].count(char) >= lower and pwd[2].count(char) <= upper:
        count += 1
print(count)

print("\n========== PART 2 ==========")

count = 0
for pwd in arr:
    lower = int(pwd[0].split("-")[0])
    upper = int(pwd[0].split("-")[1])
    char = pwd[1][0]
    if pwd[2][lower-1] == char and pwd[2][upper-1] != char:
        count += 1
    elif pwd[2][lower-1] != char and pwd[2][upper-1] == char:
        count += 1
print(count)
