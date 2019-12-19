n = int(input())
teas = [int(x) for x in input().split()]
input()
toppings = [int(x) for x in input().split()]
ans = []
for tea in teas:
    topping_indices = [int(x) for x in input().split()[1:]]
    cheapest_topping = min(toppings[i-1] for i in topping_indices)
    ans.append(tea + cheapest_topping)
print(max(0, int(input()) // min(ans) - 1))
