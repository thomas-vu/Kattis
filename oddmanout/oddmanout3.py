for tc in range(int(input())):
    input()
    inp = input().split()
    seen = dict.fromkeys(set(inp), 0)
    for x in inp:
        if seen[x]>0:
            seen.pop(x)
        else:
            seen[x] += 1
    print(f'Case #{tc+1}: {list(seen.keys())[0]}')
