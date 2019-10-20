n = int(input())
while n != 0:
	register = ['?'] * 32
	
	for _ in range(n):
		line = input()
		try:
			ins, i = line.split()
			i = int(i)
		except:
			ins, i, j = line.split()
			i, j = int(i), int(j)
	
		if ins == 'SET':
			register[i] = '1'
		elif ins == 'CLEAR':
			register[i] = '0'
		elif ins == 'OR':
			if register[i] == '1' or register[j] == '1':
				register[i] = '1'
			elif register[i] == '0' and register[j] == '0':
				register[i] = '0'
			else:
				register[i] = '?'
		else:
			if register[i] == '0' or register[j] == '0':
				register[i] = '0'
			elif register[i] == '1' and register[j] == '1':
				register[i] = '1'
			else:
				register[i] = '?'
	
	print(''.join(reversed(register)))
	n = int(input())
