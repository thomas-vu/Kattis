for _ in range(int(input())):
    line = input()
    n = len(line)
    for i in range(1, n+1):
        if line == (line[:i]*n)[:n]:
            print(i)
            break
