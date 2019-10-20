S = set()
for word in input().split():
	if word in S:
		print('no')
		exit()
	S.add(word)
print('yes')
