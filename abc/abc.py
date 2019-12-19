numbers = [int(i) for i in input().split()]
order = input()

numbers.sort()

for ch in order:
    if ch == "A":
        print(numbers[0])
    if ch == "B":
        print(numbers[1])
    if ch == "C":
        print(numbers[2])
