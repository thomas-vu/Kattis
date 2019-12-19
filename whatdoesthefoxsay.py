for _ in range(int(input())):
    recording = input().split()
    notfox = set()
    line = input()
    while line != 'what does the fox say?':
        notfox.add(line.split()[-1])
        line = input()
    print(' '.join(sound for sound in recording if sound not in notfox))
