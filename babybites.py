n = int(input())
counting = [x for x in input().split()]
for i, x in zip(range(1, n+1), counting):
    if x != 'mumble' and int(x) != i:
        print('something is fishy')
        raise SystemExit
print('makes sense')
