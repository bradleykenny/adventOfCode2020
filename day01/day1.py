import math

print("========== PART 1 ==========")

inFile = open("day1.txt")

arr = [int(line) for line in inFile]
n = len(arr)

ans = 0
for i in range(n):
	for j in range(i+1, n):
		if (arr[i] + arr[j] == 2020):
			ans = [ arr[i], arr[j], (arr[i] * arr[j]) ]

print(ans)

print("\n========== PART 2 ==========")

ans = 0
for i in range(n):
	for j in range(i+1, n):
		for k in range(j+1, n):
			if ((arr[i] + arr[j] + arr[k]) == 2020):
				ans = [ arr[i], arr[j], arr[k], (arr[i] * arr[j] * arr[k]) ]
				
print(ans)