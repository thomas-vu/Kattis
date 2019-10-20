word = set(input())
guesses = input()

hangman = 0
for c in guesses:
	if c in word:
		word.remove(c)
		if not word:
			print('WIN')
			exit()
	else:
		hangman += 1
		if hangman == 10:
			print('LOSE')
			exit()
