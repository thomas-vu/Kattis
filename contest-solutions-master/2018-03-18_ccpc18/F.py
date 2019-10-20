P, T = map(int, input().split())
print(sum(1 for _ in range(P) if all([input()[1:].islower() for _ in range(T)])))