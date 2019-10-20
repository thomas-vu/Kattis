coins = [1, 2, 5, 10]

5
2 2 1
2 1 1 1
1 1 1 1 1

10
5 5
5 2 2 1
5 2 1 1 1
5 1 1 1 1 1
2 2 2 2 2
2 2 2 2 1 1
2 2 2 1 1 1 1
2 2 1 1 1 1 1 1
2 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1

memo = {}
def solve(amount):
	if amount <= 0:
		return 0
	if amount not in memo:
		sol = 0
		for coin in coins:
			sol += 1 + solve(amount - coin)
		memo[amount] = sol
	return memo[amount]

print(solve(5))
