input()
dirty = [int(x) for x in input().split()]

dirtiness = 0
howmanydirty = 0
cleanups = 0
nextdirty = dirty.pop(0)
for day in range(1, 366):
    if day == nextdirty:
        howmanydirty += 1
        nextdirty = dirty.pop(0) if dirty else 366
    if dirtiness + howmanydirty >= 20:
        dirtiness = 0
        howmanydirty = 0
        cleanups += 1
    dirtiness += howmanydirty

print(cleanups if dirtiness == 0 else cleanups+1)
