right = int(input())
you = input()
friend = input()
wrong = len(you) - right
match = sum(1 for y, f in zip(you, friend) if y == f)
no_match = len(you) - match
print(min(right, match) + min((wrong, no_match)))
