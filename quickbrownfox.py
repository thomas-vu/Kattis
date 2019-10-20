from string import ascii_lowercase
for _ in range(int(input())):
	alphabet = set(ascii_lowercase)
	line = set(input().lower())
	diff = alphabet - line
	print('missing ' + ''.join(sorted(diff)) if diff else 'pangram')
