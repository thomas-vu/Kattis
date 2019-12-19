for _ in range(int(input())):
    k = int(input())
    name = input()
    menu = [input() for _ in range(k)]
    if 'pea soup' in menu and 'pancakes' in menu:
        print(name)
        exit()
print('Anywhere is fine I guess')
