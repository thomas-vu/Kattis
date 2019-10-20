n = int(input())
while n != 0:
	times = []
	original = {}
	for _ in range(n):
		HM, ampm = input().split()
		H, M = [int(x) for x in HM.split(':')]
		converted = (0 if H == 12 else H) * 60 + M + (720 if ampm == 'p.m.' else 0)
		times.append(converted)
		original[converted] = HM + ' ' + ampm
	for time in sorted(times):
		print(original[time])
	print()
	n = int(input())
