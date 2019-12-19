n = int(input())
papers = sorted(int(input()) for _ in range(n))
ans = 0
#print(papers)
for i in range(n):
    if papers[i] <= len(papers)-i:
        ans = papers[i]
    if papers[i] > len(papers)-i:
        ans = max(ans, len(papers)-i)
print(ans)
