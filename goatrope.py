#7 3 0 0 5 4
#.............
#.............
#.............
#-----x.......
#.....|.g.....
#.....|.......
#.....|.......
#.....|.......

from math import sqrt
x, y, x1, y1, x2, y2 = [int(x) for x in input().split()]
if x1 <= x <= x2:
    print(min(abs(y-y1), abs(y-y2)))
elif y1 <= y <= y2:
    print(min(abs(x-x1), abs(x-x2)))
elif x < x1:
    if y > y2:
        print(sqrt((x-x1)**2 + (y-y2)**2))
    else:
        print(sqrt((x-x1)**2 + (y-y1)**2))
else:
    if y > y2:
        print(sqrt((x-x2)**2 + (y-y2)**2))
    else:
        print(sqrt((x-x2)**2 + (y-y1)**2))
