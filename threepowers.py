n = int(input())
while n != 0:
    subset = []
    for i, bit in enumerate(reversed(bin(n-1)[2:])):
        if bit == '1':
            subset.append(str(3**i))
    print('{ }' if n == 1 else '{ ' + ', '.join(subset) + ' }')
    n = int(input())
