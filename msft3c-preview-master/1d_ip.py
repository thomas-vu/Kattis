def ip2long(ip):
    r = 0L
    for part in ip.split('.'):
        r <<= 8
        r |= long(part)
    return r

def process(s):
    a, b, c = s.split()
    if any(not part.isdigit() or int(part) < 0 or int(part) > 255 for part in c.split('.')):
        return 'InValid'
    a, b, c = map(ip2long, (a, b, c))
    return 'InRange' if a <= c <= b else 'OutRange'

while True:
    print(process(raw_input()))
    try:
        print(process(raw_input()))
    except:
        break
