for y in range(int(input())):
	input()
	guests = input().split()
	oddone = (x for x in guests if guests.count(x) == 1)
	print(f'Case #{y+1}: {next(oddone)}')
