import math
n, k = [int(x) for x in input().split()]
print(math.factorial(n) - math.factorial(n-1))
