import fractions
import decimal
import math
def solve(i, exp):
	if i >= n:
		return 0
	if (i, exp) not in memo:
		sol = min(courses[i], int(m*(2/3)**exp)) + solve(i+1, exp+1)
		sol = max(sol, solve(i+1, max(0, exp-1)))
		sol = max(sol, solve(i+2, 0))
		memo[(i, exp)] = sol
	return memo[(i, exp)]

n, m = [int(x) for x in input().split()]
courses = [int(x) for x in input().split()]
memo = {}
print(solve(0, 0))
