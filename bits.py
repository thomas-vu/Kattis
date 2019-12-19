for _ in range(int(input())):
    X = input()
    ans = 0
    for i in range(1, len(X)+1):
        ans = max(ans, bin(int(X[:i])).count('1'))
    print(ans)
