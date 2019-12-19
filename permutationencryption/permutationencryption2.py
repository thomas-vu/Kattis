from sys import stdin
for line in stdin:
    if line == '0\n': break

    lk, *key = [int(x) for x in line.split()]
    msg = input()
    lm = len(msg)
    msg += ' ' * (0 if lm % lk == 0 else lk - (lm % lk))
    msg = [msg[i:i+lk] for i in range(0, lm, lk)]
    msg = [slc[x-1] for slc in msg for x in key]
    print("'" + ''.join(msg) + "'")
