from functools import reduce
n = int(input())
while n != 0:
    S = set()
    files = []
    for _ in range(int(n)):
        line = input()
        S.add(line)
        files.append((line, reduce(lambda x, y: x ^ ord(y), line, 0)))
    collisions = 0
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            if files[i][1] == files[j][1] and files[i][0] != files[j][0]:
                collisions += 1
    print(len(S), collisions)
    n = int(input())
