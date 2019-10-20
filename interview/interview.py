def solve(A, B, T, i):
	if i == len(offers):
		return 0
	a, b = offers[i]
	a_gain = max(0, a-A)
	b_gain = max(0, b-B)
	new_T = T - a_gain*ta - b_gain*tb
	if new_T >= 0:
		take = 1 + solve(A+a_gain, B+b_gain, new_T, i+1)
		dont = solve(A, B, T, i+1)
		return max(take, dont)
	else:
		return solve(A, B, T, i+1)
	
A, B, T, ta, tb = [int(x) for x in input().split()]
offers = []
for _ in range(int(input())):
	a, b = [int(x) for x in input().split()]
	offers.append((a, b))
print(solve(A, B, T, 0))
