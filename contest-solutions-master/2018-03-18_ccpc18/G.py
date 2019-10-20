N, M = map(int, input().split())
essay = input().split()

P = [x for x in range(10000)] # parent
S = [1] * 10000 # size
D = [1000] * 10000 # best word size
def unite(a, b, v):
	global P
	global S
	global D
	a = find(a)
	b = find(b)
	if a == b:
		D[a] = min(D[a], v)
		return
	if S[a] < S[b]:
		a, b = b, a
	S[a] += S[b]
	D[a] = min(D[a], D[b], v)
	P[b] = a

def find(x):
	global P
	if x != P[x]:
		P[x] = find(P[x])
	return P[x]

id = {}
n = 0
for _ in range(M):
	a, b = input().split()
	if a not in id:
		id[a] = n
		n += 1
	if b not in id:
		id[b] = n
		n += 1
	unite(id[a], id[b], min(len(a), len(b)))

total = 0
for w in essay:
	if w in id:
		total += D[find(id[w])]
	else:
		total += len(w)

print(total)