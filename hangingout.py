L, x = [int(x) for x in input().split()]
ans = 0
current = 0
for _ in range(x):
    e, n = input().split(); 
    n = int(n)
    if e == 'enter':
        if current + n > L:
            ans += 1
        else:
            current += n
    else:
        current -= n
print(ans)
