n = int(input())
wo, bo, wd, bd, *queue = input().split()
white = [wo, wd]
black = [bo, bd]

record = 0
winners = []

dynasty = ''
streak = 0
for point in input():
    if point == 'W':
        if dynasty == 'W':
            streak += 1
        else:
            dynasty = 'W'
            streak = 1

        if streak > record:
            record = streak
            winners = [white]
        elif streak == record:
            winners.append(white)

        wo, wd = wd, wo
        queue.append(bd)
        bo, bd = queue.pop(0), bo
        black = [bd, bo]
    else:
        if dynasty == 'B':
            streak += 1
        else:
            dynasty = 'B'
            streak = 1

        if streak > record:
            record = streak
            winners = [black]
        elif streak == record:
            winners.append(black)

        bo, bd = bd, bo
        queue.append(wd)
        wo, wd = queue.pop(0), wo
        white = [wd, wo]

for a, b in winners:
    print(a, b)
