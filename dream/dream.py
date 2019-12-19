# missing the case where X Just A Dream would undo an event
# that the scenario claims to happen, leading to a Plot Error

d = {}
D = []
n = 0
for _ in range(int(input())):
    line = input().split()
    if line[0] == 'E':
        e = line[1]
        d[e] = n
        D.append(e)
        n += 1
    elif line[0] == 'D':
        r = int(line[1])
        for _ in range(r):
            del d[D.pop()]
        n -= r
    else:
        earliest = n
        events = line[2:]
        for event in events:
            if event[0] == '!':
                event = event[1:]
                if event in d and d[event] < earliest:
                    earliest = d[event]
            elif event not in d:
                print('Plot Error')
                break
        else:
            print(f'{n-earliest} Just A Dream' if n-earliest else 'Yes')
