for tc in range(int(input())):
	input()
	S = set()
	for x in input().split():
		if x in S:
			S.remove(x)
		else:
			S.add(x)
	print(f'Case #{tc+1}: {S.pop()}')
