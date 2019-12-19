input()
L = input()
match = {')': '(', ']': '[', '}': '{'}
stack = []
for i, ch in enumerate(L):
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if not stack or stack.pop() != match[ch]:
            print(ch, i)
            exit()
print('ok so far')
