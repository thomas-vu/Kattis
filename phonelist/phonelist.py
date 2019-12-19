from collections import defaultdict

def tree():
    return defaultdict(tree)

for _ in range(int(input())):
    phonelist = tree()
    consistent = True
    for _ in range(int(input())):
        number = input()
        if not consistent:
            continue
        node = phonelist
        for i, digit in enumerate(number):
    
            # end of current string
            if i+1 == len(number):
                if digit in node:            # ending on trodden path
                    consistent = False
                else:                        # ended as new path
                    node[digit] = 'end'
    
            # string continues
            elif node[digit] == 'end':         # dead end node
                consistent = False
            elif digit in node:             # following a path
                node = node[digit]
    
    print('YES' if consistent else 'NO')
