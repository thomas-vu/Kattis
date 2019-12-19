def main():
    from sys import stdin
    lines = stdin.readlines()
    offset = 0
    while True:
        N, M = [int(x) for x in lines[offset].split()]
        if N + M == 0:
            break
        offset += 1
        jack = set(lines[offset:offset+N])
        jill = set(lines[offset+N:offset+N+M])
        print(len(jack & jill))
        offset += N + M

main()
