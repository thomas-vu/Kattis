A, B = [int(x) for x in input().split()]
while A != 0:
	Ai, Bi = A, B
	sA, sB = 0, 0
	dA, dB = {A: sA}, {B: sA}

	while Ai != 1:
		if Ai % 2 == 0:
			Ai //= 2
		else:
			Ai = Ai*3+1
		sA += 1
		dA[Ai] = sA
		
	while Bi != 1:
		if Bi % 2 == 0:
			Bi //= 2
		else:
			Bi = Bi*3+1
		sB += 1
		dB[Bi] = sB

	for C in dA:
		if C in dB:
			sA = dA[C]
			sB = dB[C]
			break
	
	print(f'{A} needs {sA} steps, {B} needs {sB} steps, they meet at {C}')
	A, B = [int(x) for x in input().split()]
