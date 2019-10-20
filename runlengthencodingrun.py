op, msg = [x for x in input().split()]
ans = ''
if op == 'E':
	run = 0
	for i, ch in enumerate(msg):
		run += 1
		if i == len(msg)-1:
			ans += ch + str(run)
		elif msg[i] != msg[i+1]:
			ans += ch + str(run)
			run = 0
else:
	for ch, run in (msg[i:i+2] for i in range(0, len(msg), 2)):
		ans += ch * int(run)
print(ans)
