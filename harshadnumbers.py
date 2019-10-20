n = int(input())
while n % sum(map(int, str(n))) != 0:
	n += 1
print(n)
