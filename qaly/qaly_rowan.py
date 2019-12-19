qaly = int(input())
finalNumber = 0.0
qalyNums = []
for _ in range(qaly):
    qalyBoth = str(input()).split()
    qalyNums.append(qalyBoth)

for x, y in enumerate(qalyNums):
    finalNumber = finalNumber + (float(qalyNums[x][0]) * float(qalyNums[x][1]))


print(finalNumber)
