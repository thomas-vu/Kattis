n, e, d = [int(x) for x in input().split()]
E = sorted([int(x) for x in input().split()])[::-1]
D = sorted([int(x) for x in input().split()])[::-1]

kittens = 0
players = [[i, 0] for i in range(n)]

pos = 0 # deck pos
i = 0   # current player

print(E)
print(D)
while len(players) > 1:
    print(kittens)
    currentpopped = False
    card = ''
    if pos == E[-1]:
        card = 'EK'
        E.pop()
        kittens += 1
        if kittens == e:
            break
    elif D and pos == D[-1]:
        card = 'D'
        D.pop()

    if card == 'EK':
        if players[i][1] != 0:
            players[i][1] -= 1
        else:
            players.pop(i)
            currentpopped = True
    elif card == 'D':
        players[i][1] += 1

    if not currentpopped:
        if players[i][1] > 5:
            players[i][1] -= 1

    if currentpopped:
        if i == len(players):
            i = 0
    elif i == len(players)-1:
        i = 0
    else:
        i += 1
    pos += 1

if len(players) == 1:
    print(players[0][0])
else:
    print(-1)
