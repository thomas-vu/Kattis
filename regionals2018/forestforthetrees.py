from fractions import Fraction

def CheckWithin(cx, cy):
    return cx >= x1 and cx <= x2 and cy >= y1 and cy <= y2

xbelle, ybelle = [int(x) for x in input().split()]
x1, y1, x2, y2 = [int(x) for x in input().split()]

frac = Fraction(xbelle, ybelle)
#print(frac.numerator, frac.denominator)

num_points = xbelle // frac.numerator
#print(num_points)

i = 1
while i < num_points:
    #print(i)
    checkX, checkY = frac.numerator*i, frac.denominator*i
    #print(checkAt)
    if CheckWithin(checkX, checkY):
        num_rise_points = y2 // checkY
        num_run_points = x2 // checkX
        #print(num_rise_points, num_run_points)
        i += min(num_rise_points, num_run_points)
    else:
        print('No')
        print(checkX, checkY)
        raise SystemExit
print('Yes')