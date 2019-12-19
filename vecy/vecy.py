import itertools
X = input()
a = [int(''.join(x)) for x in itertools.permutations(X)]
b = [x for x in a if x > int(X)]
print(min(b) if len(b) != 0 else 0)
