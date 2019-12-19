n, m = [int(x) for x in input().split()]
T = sorted(int(x) for x in input().split())
L = sorted(int(x) for x in input().split())

completed = 0
i = 0
j = 0

while j < m:
    if T[i] <= L[j]:
        completed += 1
        i += 1
    j += 1

print(completed)
