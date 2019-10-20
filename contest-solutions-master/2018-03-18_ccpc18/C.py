for r in range(8):
	for c, v in enumerate(input()):
		if v == 'K':
			Kr, Kc = r, c
		elif v == 'R':
			Rr, Rc = r, c
		elif v == 'k':
			kr, kc = r, c

kingMoves = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def check(Kr, Kc, Rr, Rc, kr, kc):
	return any(Kr + a == kr and Kc + b == kc for a, b in kingMoves) or \
		Rr == kr and Rc != kc or \
		Rc == kc and Rr != kr

def checkmate(Kr, Kc, Rr, Rc, kr, kc):
	# Invalid move: out of bounds
	if not (0 <= Rr < 8 and 0 <= Rc < 8): # 0 <= Kr < 8 and 0 <= Kc < 8
		return False

	if not check(Kr, Kc, Rr, Rc, kr, kc):
		return False

	# Opponent can escape check
	for a, b in kingMoves:
		if 0 <= kr + a < 8 and 0 <= kc + b < 8:
			if not check(Kr, Kc, Rr, Rc, kr + a, kc + b):
				return False
	return True

# any(checkmate(Kr + a, Kc + b, Rr, Rc, kr, kc) for a, b in kingMoves) or
c = any (
	checkmate(Kr, Kc, Rr+d, Rc, kr, kc) for d in range(-7, 7+1)
) or any (
	checkmate(Kr, Kc, Rr, Rc+d, kr, kc) for d in range(-7, 7+1)
)

print('Yes' if c else 'No')