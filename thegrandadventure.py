for _ in range(int(input())):
    a = input()
    match = {'b': '$', 't': '|', 'j': '*'}
    stack = []
    for ch in a:
        if ch in '$|*':
            stack.append(ch)
        elif ch in 'btj':
            if not stack or stack.pop() != match[ch]:
                print('NO')
                break
    else:
        print('NO' if stack else 'YES')
