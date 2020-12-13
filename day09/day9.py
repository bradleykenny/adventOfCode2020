
print("========== PART 1 ==========")

inFile = open("day9.txt")

arr = [int(line.replace("\n", "")) for line in inFile]
n = len(arr)

invalidNum = 0
for i in range(25, n):
    pre = arr[i-25:i]
    valid = False

    for j in pre:
        for k in pre:
            if j + k == arr[i]:
                valid = True
    
    if not valid:
        invalidNum = arr[i]
        break

print(invalidNum)

print("\n========== PART 2 ==========")

for i in range(0, n):
    total = arr[i]
    j = i
    numbers = [arr[i]]
    while total < invalidNum:
        i += 1
        numbers.append(arr[i])
        total += arr[i]
    if total == invalidNum:
        smallest = numbers[0]
        largest = numbers[0]
        for o in numbers:
            if o < smallest:
                smallest = o
            if o > largest:
                largest = o
        print(smallest + largest)
        break