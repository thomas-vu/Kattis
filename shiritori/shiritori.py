n = int(input())
word = input()
prev = word[-1]
history = set([word])
for i in range(n-1):
	word = input()
	if word[0] != prev or word in history:
		print(f'Player {i%2 or 2} lost')
		exit()
	prev = word[-1]
	history.add(word)
print('Fair Game')
