L = int(input())
D = int(input())
X = int(input())

for x in range(L, D+1):
    digitsum = 0
    for digit in str(x):
        digitsum += int(digit)
    if digitsum == X:
        print(x)
        break

for x in range(D, L-1, -1):
    digitsum = 0
    for digit in str(x):
        digitsum += int(digit)
    if digitsum == X:
        print(x)
        break
