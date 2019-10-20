def main():
	from sys import stdin
	for _ in range(int(stdin.readline())):
		N, D = [int(x) for x in stdin.readline().split()]
		H = [int(x) for x in stdin.readline().split()]
		E = [int(x) for x in stdin.readline().split()]
		
		prev = ans = (H[0] + D - 1) // D

		if N > 1:
			case1 = ans + max(0, (H[1] - E[0] + D - 1) // D)
			init = max(0, (H[1] + D - 1) // D)
			REO = max(0, (H[0] - E[1] + D - 1) // D)
			remaining = REO
			ans = min(case1, init+REO)
		
		for i in range(2, N):
			case1 = ans + max(0, (H[i] - E[i-1] + D - 1) // D)
			init = max(0, (H[i] + D - 1) // D)
			REO = max(0, (H[i-1] - E[i] + D - 1) // D)
			BSE = max(0, (H[i-1] - E[i] - E[i-2] + D - 1) // D)
			prev, ans, remaining = ans, min(case1, init+REO+remaining, init+prev+BSE), min(REO+remaining, prev+BSE)
		
		print(ans)

main()
