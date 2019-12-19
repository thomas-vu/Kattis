import json
from collections import defaultdict
def tree(): return defaultdict(tree)

n, _ = [int(x) for x in input().split()]
shapes = []
for _ in range(n):
    ceiling = tree()
    layers = [int(x) for x in input().split()]
    node = layers[0]
    ceiling[node]
    for l in layers[1:]:
        if l < node:
            ceiling[node][l]
            node = l
            print(json.dumps(ceiling))
        else:
            ceiling[node][l]
            node = l
            print(json.dumps(ceiling))

#idk wtf im doing
