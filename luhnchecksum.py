for _ in range(int(input())):
    n = input()
    ans = ''
    for i, d in enumerate(n[::-1]):
        if i % 2 == 1:
            d = int(d) * 2
            if d > 9:
                d = int(str(d)[0]) + int(str(d)[1])
        ans += str(d)
    print('PASS' if sum(int(x) for x in ans) % 10 == 0 else 'FAIL')
