n, _ = [int(x) for x in input().split()]
commands = [x for x in input().split()]

positions = []
current = 0
undoing = False
for command in commands:

	if command == 'undo':
		undoing = True
		continue
	
	command = int(command)
	if undoing:
		undoing = False
		for _ in range(command):
			positions.pop()
		current = positions[-1] if positions else 0
	else:
		newcurrent = (current + command) % n
		positions.append(newcurrent)
		current = newcurrent

print(current)

#def main():
#    n, k = map(int, input().split())
#    history = [0]
#    moves = list(input().split())
#
#    undo = False
#    for move in moves:
#        if move == 'undo':
#            undo = True
#        elif undo:
#            undo = False
#            x = int(move)
#            for _ in range(x):
#                history.pop()
#        else:
#            x = int(move)
#            history.append((history[-1] + 3 * n + x) % n)
#
#    print(history[-1])
#
#main()
