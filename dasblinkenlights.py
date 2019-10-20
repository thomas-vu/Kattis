import math
p, q, s = [int(x) for x in input().split()]
print('yes' if p*q/math.gcd(p, q) <= s else 'no')
