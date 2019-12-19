_, m = [int(x) for x in input().split()]
courses = [int(x) for x in input().split()]

dp = [(0, True), (min(courses[0], m), False)]

for c in courses[1:]:
    newdp = [(0, False) for _ in range(len(dp)+1)]
    for i, ans in enumerate(dp):
        val, S = ans
        if S and val >= newdp[0][0]:
            newdp[0] = (val, True)
        elif i != 0 and val >= newdp[i-1][0]:
            newdp[i-1] = (val, True)
        newdp[i+1] = (val + min(c, int(m*(2/3)**i)), False)
        print(newdp)
    dp = newdp
    print()

print(max(dp)[0])

# 900 600 400 266 177 118
# 348
#      381
#          400
#      <
# <
# 869
# <
# 306
#       600

# I get 2848 instead of 2904.
