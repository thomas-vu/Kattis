def process(s):
    buf = []
    count = 0
    prev = ''
    for c in s:
        if c == prev:
            count += 1
        else:
            if count >= 2:
                buf.append(str(count))
            buf.append(prev)

            count = 1
            prev = c

    if count >= 2:
        buf.append(str(count))
    buf.append(prev)

    return ''.join(buf)

# This also works

#import re
#PATTERN = re.compile(r'([a-zA-Z])\1+')
#def process(s):
#    return PATTERN.sub(lambda m: str(len(m.group(0))) + m.group(1), s)

N = int(raw_input())
print(N)
for _ in xrange(N):
    print(process(raw_input()))
