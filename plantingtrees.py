print(max(x + i for i, x in zip(range(int(input())), sorted(int(x) for x in input().split())[::-1])) + 2)
# rewrite with enumerate
