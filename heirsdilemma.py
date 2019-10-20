L, H = [int(x) for x in input().split()]
print(sum(1 for x in range(L, H+1) if ('0' not in str(x)
										and len(set(str(x))) == 6
										and x % int(str(x)[0]) == 0
										and x % int(str(x)[1]) == 0
										and x % int(str(x)[2]) == 0
										and x % int(str(x)[3]) == 0
										and x % int(str(x)[4]) == 0
										and x % int(str(x)[5]) == 0)))
