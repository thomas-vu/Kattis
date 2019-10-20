B = [[c == 'k' for c in input()] for _ in range(5)]
K = {(r, c) for c in range(5) for r in range(5) if B[r][c]}
fail = any((r-1, c-2) in K or (r-1, c+2) in K or (r+1, c-2) in K or (r+1, c+2) in K or
				(r-2, c-1) in K or (r-2, c+1) in K or (r+2, c-1) in K or (r+2, c+1) in K
				for r, c in K)
print('invalid' if fail else 'valid')