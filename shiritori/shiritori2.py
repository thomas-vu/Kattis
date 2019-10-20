def main():
	from sys import stdin
	n = int(stdin.readline())
	word = stdin.readline()
	prev = word[-2]
	history = set([word])
	for i in range(n-1):
		word = stdin.readline()
		if word[0] != prev or word in history:
			print(f'Player {i%2 or 2} lost')
			break
		prev = word[-2]
		history.add(word)
	else:
		print('Fair Game')
main()
