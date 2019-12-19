print([1 for a, b in zip(input(), 'PER' * 100) if a != b])
print([1 if a != b else 0 for a, b in zip(input(), 'PER' * 100)])

print(sum(1 for a, b in zip(input(), 'PER' * 100) if a != b))
print(sum(1 if a != b else 0 for a, b in zip(input(), 'PER' * 100)))

# golfed
print(sum(1for a,b in zip(input(),'PER'*100)if a!=b))
print(sum(1if a!=b else 0for a,b in zip(input(),'PER'*100)))
