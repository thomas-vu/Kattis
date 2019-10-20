# 5:35 pm to 6:02 pm = 27 minutes

C, L, V = map(int, raw_input().split())

c = [raw_input() for _ in range(C)]
v = raw_input()

def longest_match(a, b):
    # longest substring in a that matches subsequence in b
    best = 0
    for i in range(len(a)):
        for j in range(len(b)):
            cur = 0
            ii = i
            jj = j
            while ii < len(a) and jj < len(b):
                if a[ii] == b[jj]:
                    ii += 1
                    cur += 1
                jj += 1
            if best < cur:
                best = cur
    return best

citizen_value = map(lambda x: longest_match(x, v), c)
sorted_ranks = sorted(set(citizen_value), reverse=True)
value_to_rank = {v: i+1 for i, v in enumerate(sorted_ranks)}

for i, citizen_rank in enumerate(citizen_value):
    print('Person #{}: {}.'.format(i, value_to_rank[citizen_rank]))
