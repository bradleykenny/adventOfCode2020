import copy
import re

print("========== PART 1 ==========")

inFile = open("day4.txt")

arr = [line.replace("\n", "") for line in inFile]
n = len(arr)

defaultPassport = {
    "byr": False,
    "iyr": False,
    "eyr": False,
    "hgt": False,
    "hcl": False,
    "ecl": False,
    "pid": False,
    "cid": False
}

currPassport = copy.deepcopy(defaultPassport)
total = 0
for line in arr:
    if line == "":
        for item in currPassport:
            if item == "cid":
                continue
            elif currPassport[item] == False:
                total -= 1
                break
        total += 1
        currPassport = copy.deepcopy(defaultPassport)
    for cred in line.split(" "):
        currPassport[cred.split(":")[0]] = True

print(total)

print("\n========== PART 2 ==========")

currPassport = copy.deepcopy(defaultPassport)
total = 0
for line in arr:
    if line == "":
        for item in currPassport:
            if item == "cid":
                continue
            elif currPassport[item] == False:
                total -= 1
                break
        total += 1
        currPassport = copy.deepcopy(defaultPassport)
    for cred in line.split(" "):
        value = cred.split(":")
        if value[0] == "byr":
            byr = int(value[1])
            if byr >= 1920 and byr <= 2002:
                currPassport[value[0]] = True
        elif value[0] == "iyr":
            iyr = int(value[1])
            if iyr >= 2010 and iyr <= 2020:
                currPassport[value[0]] = True
        elif value[0] == "eyr":
            eyr = int(value[1])
            if eyr >= 2020 and eyr <= 2030:
                currPassport[value[0]] = True
        elif value[0] == "hgt":
            if len(value[1]) > 2:
                hgt = [int(value[1][:-2]), value[1][-2:]]
                if hgt[1] == "cm" and hgt[0] >= 150 and hgt[0] <= 193:
                    currPassport[value[0]] = True
                if hgt[1] == "in" and hgt[0] >= 59 and hgt[0] <= 76:
                    currPassport[value[0]] = True
        elif value[0] == "hcl":
            match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value[1])
            if match:
                currPassport[value[0]] = True
        elif value[0] == "ecl":
            validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if value[1] in validEcl:
                currPassport[value[0]] = True
        elif value[0] == "pid":
            match = re.search(r'^[0-9]{9}$', value[1])
            if match:
                currPassport[value[0]] = True

print(total)
