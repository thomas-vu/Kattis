try:
    words = []
    while True:
        words += input().split()
except EOFError as e:
    compound = set()
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            compound.add(words[i] + words[j])
            compound.add(words[j] + words[i])
    print('\n'.join(sorted(compound)))
