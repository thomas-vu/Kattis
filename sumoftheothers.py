from sys import stdin
for line in stdin:
    A = [int(x) for x in line.split()]
    print(sum(A)//2)

# golfed
import sys
for a in sys.stdin:print(sum(map(int,a.split()))//2)
