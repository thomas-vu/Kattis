N, K = [int(x) for x in input().split()]
if K == 0:
    print(0)
    raise SystemExit
safe = [int(input()) for _ in range(K)]

ans = 0
pointer = 0
for i in range(1, N+1):
    if i > safe[pointer]:
        pointer += 1
        if pointer == K:
            break
    ans += N - safe[pointer] + 1
print(ans)
