from collections import Counter

cnt = Counter()
for _ in range(int(input())):
	cnt[input()] += 1

fewest = min(cnt.values())
ans = [key for key in cnt if cnt[key] == fewest]
print('\n'.join(sorted(ans)))
