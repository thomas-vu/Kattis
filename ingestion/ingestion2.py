def solve(i, exp, skippedprev):
	if i >= n:
		return 0
	if (i, exp, skippedprev) not in memo:
		sol = min(courses[i], int(m*(2/3)**exp)) + solve(i+1, exp+1, False)
		if skippedprev:
			sol = max(sol, solve(i+1, 0, True))
		else:
			sol = max(sol, solve(i+1, max(0, exp-1), True))
		memo[(i, exp, skippedprev)] = sol
	return memo[(i, exp, skippedprev)]

n, m = [int(x) for x in input().split()]
courses = [int(x) for x in input().split()]
memo = {}
print(solve(0, 0, False))
