stuck = int(input())
branches = []
while(True):
    uh = input()
    if uh == "-1":
        break
    branches.append([int(i) for i in uh.split()])

solutin = [stuck]
uh = True
while(uh):
    uh = False
    for b in branches:
        if stuck in b and b[0] != stuck:
            solutin.append(b[0])
            stuck = b[0]    
            uh = True

print(" ".join(str(i) for i in solutin))
