from fractions import Fraction

xb, yb = [int(x) for x in input().split()]
x1, y1, x2, y2 = [int(x) for x in input().split()]
frac = Fraction(xb, yb)
num_points = xb // frac.numerator

i = 1
while i < num_points:
    x, y = frac.numerator*i, frac.denominator*i
    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
        i += min(y2 // y, x2 // x)
    else:
        print('No')
        print(x, y)
        raise SystemExit
print('Yes')
