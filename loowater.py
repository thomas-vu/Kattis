while True:
	h, k = [int(x) for x in input().split()]
	if h == 0:
		break
	heads = sorted(int(input()) for _ in range(h))
	knights = sorted(int(input()) for _ in range(k))
	
	coins = 0
	i = 0
	j = 0
	
	while j < k:
		if heads[i] <= knights[j]:
			coins += knights[j]
			i += 1
			if i == h:
				print(coins)
				break
		j += 1
	else:
		print('Loowater is doomed!')
