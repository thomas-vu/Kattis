def solve(page):
    if book[page] == ['favourably']:
        return 1
    if book[page] == ['catastrophically']:
        return 0
    if page not in memo:
        memo[page] = solve(book[page][0]) + solve(book[page][1]) + solve(book[page][2])
    return memo[page]

for _ in range(int(input())):
    memo = {}
    book = {}
    for _ in range(int(input())):
        page, *content = input().split()
        book[page] = content
    print(solve('1'))
