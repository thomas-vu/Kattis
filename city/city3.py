def main():
	from math import ceil
	for _ in range(int(raw_input())):
		N, D = [int(x) for x in raw_input().split()]
		H = [int(x) for x in raw_input().split()]
		E = [int(x) for x in raw_input().split()]
		
		prev = ans = ceil(H[0] / D)

		if N != 1:
			case1 = ans + max(0, ceil((H[1] - E[0]) / D))
			init = max(0, ceil(H[1] / D))
			REO = max(0, ceil((H[0] - E[1]) / D))
			remaining = REO
			ans = min(case1, init+REO)
		
		for i in range(2, N):
			case1 = ans + max(0, ceil((H[i] - E[i-1]) / D))
			init = max(0, ceil(H[i] / D))
			REO = max(0, ceil((H[i-1] - E[i]) / D))
			BSE = max(0, ceil((H[i-1] - E[i] - E[i-2]) / D))
			prev, ans, remaining = ans, min(case1, init+REO+remaining, init+prev+BSE), min(REO+remaining, prev+BSE)
		
		print ans

main()
