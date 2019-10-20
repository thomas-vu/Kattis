BS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def to_base(n, b): 
    return to_base(n//b, b).lstrip('0') + BS[n%b] if n else '0'

for _ in range(int(input())):
	tc, b, n = [int(x) for x in input().split()]
	print(tc, sum(int(d, b)**2 for d in to_base(n, b)))
