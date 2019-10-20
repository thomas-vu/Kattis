n, y = [int(x) for x in input().split()]
found = set(int(input()) for _ in range(y))
print('\n'.join(str(x) for x in range(n) if x not in found))
print(f'Mario got {len(found)} of the dangerous obstacles.')
