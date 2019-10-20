N, T = [int(x) for x in input().split()]
A, B, C, t0 = [int(x) for x in input().split()]

t = [t0]
for i in range(1, N):
	ti = ((A*t[i-1] + B) % C) + 1
	t.append(ti)

t.sort()
print(t)

solved = 0
penalty = 0
elapsed = 0
while penalty < T and solved < N:
	elapsed += t[solved]
	penalty += elapsed
	solved += 1
print(solved, penalty)
