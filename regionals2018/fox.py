import string

for _ in range(int(input())):
	s = input().lower()
	a = set()
	for ch in s:
		if ch in string.ascii_lowercase:
			a.add(ch)
	if "".join(sorted(a)) == string.ascii_lowercase:
		print("pangram")
	else:
		n = []
		for ch in string.ascii_lowercase:
			if ch not in "".join(sorted(a)):
				n.append(ch)
		print("missing " + "".join(sorted(n)))


