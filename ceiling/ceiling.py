from random import shuffle

D, L, R = 'data', 'left', 'right'

def insert(tree, data):
    if tree is None:
        tree = {D: data, L: None, R: None}
    elif data <= tree[D]:
        tree[L] = insert(tree[L], data)
    else:
        tree[R] = insert(tree[R], data)
    return tree

def traverse(tree):
    if tree is not None:
        yield from traverse(tree[L])
        yield tree[D]
        yield from traverse(tree[R])

a = list(range(32))
shuffle(a)
print(a)

tree = None
for i in a:
    tree = insert(tree, i)

print(*traverse(tree))

#from collections import defaultdict
#
#def tree():
#	return defaultdict(tree)
#
#for _ in range(int(input())):
#	phonelist = tree()
#	consistent = True
#	for _ in range(int(input())):
#		number = input()
#		if not consistent:
#			continue
#		node = phonelist
#		for i, digit in enumerate(number):
#	
#			# end of current string
#			if i+1 == len(number):
#				if digit in node:			# ending on trodden path
#					consistent = False
#				else:						# ended as new path
#					node[digit] = 'end'
#	
#			# string continues
#			elif node[digit] == 'end': 		# dead end node
#				consistent = False
#			elif digit in node: 			# following a path
#				node = node[digit]
#	
#	print('YES' if consistent else 'NO')
