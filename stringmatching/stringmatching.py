from sys import stdin
for pattern in stdin:
    text = input()
    ind1 = text.find(pattern[:-1])
    progress = ind1
    ans = []
    while ind1 != -1:
        ind1 = text[ind1+1:].find(pattern[:-1])
        ind2 = ind1 + progress
        progress = ind2
        ans.append(ind1)
    print(ans)
