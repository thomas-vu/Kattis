ans = []
for _ in range(10):
    x = int(input()) % 42
    if x not in ans:
        ans.append(x)
print(len(ans))

#print(len(set(int(input()) % 42 for _ in range(10))))
