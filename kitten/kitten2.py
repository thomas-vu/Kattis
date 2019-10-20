K = input()
d = []
line = input()
while line != '-1':
	d.append(line.split())
	line = input()

ans = K
i = 0
while i < len(d):
	if K in d[i][1:]:
		K = d[i][0]
		ans += ' ' + K
		i = 0
	else:
		i += 1

print(ans)
