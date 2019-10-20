from random import randint
print('100 100')
for _ in range(100):
	s = ''
	for _ in range(100):
		s += str(randint(0, 999)) + ' '
	print(s)
