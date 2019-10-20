x, y, n = [int(x) for x in input().split()]
for i in range(1, n+1):
	ans = ''
	if i % x == 0:
		ans += 'Fizz'
	if i % y == 0:
		ans += 'Buzz'
	print(ans or i)

x, y, n = [int(x) for x in input().split()]
for i in range(1, n+1):
	print(('Fizz' if i % x == 0 else '') + ('Buzz' if i % y == 0 else '') or i)
