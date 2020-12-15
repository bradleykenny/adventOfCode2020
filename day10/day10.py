print("========== PART 1 ==========")

inFile = open("day10.txt")

arr = [int(line.replace("\n", "")) for line in inFile]
arr.append(0)

n = len(arr)
arr.sort()
arr.append(arr[n - 1] + 3)

counts = [ 0, 0, 0 ]

for i in range(1, len(arr)):
	counts[arr[i] - arr[i-1] - 1] += 1

print(counts[0] * counts[2])


print("\n========== PART 2 ==========")
