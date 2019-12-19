# The only case where stdin saves three lines is when
# the first line of each test case is unnecessary AND empty.
# Thus you cannot use it to keep the while-loop spinning -
# and must eat the input on an extra line.

# Saving three lines. (6 -> 3)
try:
    while True:
        input()
        print(input())
except:
    pass

from sys import stdin
for _ in stdin:
    print(input())

# Otherwise, using stdin always saves two lines whether or not
# the first line of each test case is necessary.

# Saving two lines. First line unnecessary. (5 -> 3)
# (See 'functionalfun' on Kattis for an example)
try:
    while input():
        print(input())
except:
    pass

from sys import stdin
for _ in stdin:
    print(input())

# Saving two lines. First line necessary. (6 -> 4)
try:
    while True:
        print(input())
        print(input())
except:
    pass

from sys import stdin
for line in stdin:
    print(line)
    print(input())
