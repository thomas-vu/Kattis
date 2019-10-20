import math
try:
	while True:
		n = int(input())
		print(1 if n <= 1 else math.floor((math.log(2*math.pi*n)/2+n*(math.log(n)-1))/math.log(10))+1)
except EOFError as e:
	pass
