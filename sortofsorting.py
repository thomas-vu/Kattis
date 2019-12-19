while True:
    n = int(input())
    if n == 0: break
    names = [input() for _ in range(n)]
    names2 = [(names[i][:2], i) for i in range(n)]
    print('\n'.join(names[i] for _, i in sorted(names2)) + '\n')
