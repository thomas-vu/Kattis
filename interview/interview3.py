import sys
sys.setrecursionlimit(2000)

def solve(A, B, T, i):
    if i == len(offers):
        return 0
    if (A, B, T, i) not in memo:
        a, b = offers[i]
        a_gain = max(0, a-A)
        b_gain = max(0, b-B)
        new_T = T - a_gain*ta - b_gain*tb
        if new_T >= 0:
            if new_T != T:
                take = 1 + solve(A+a_gain, B+b_gain, new_T, i+1)
                dont = solve(A, B, T, i+1)
                sol = max(take, dont)
            else:
                sol = 1 + solve(A, B, T, i+1)
        else:
            sol = solve(A, B, T, i+1)
        memo[(A, B, T, i)] = sol
    return memo[(A, B, T, i)]
    
A, B, T, ta, tb = [int(x) for x in input().split()]
offers = []
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    offers.append((a, b))
memo = {}
print(solve(A, B, T, 0))
