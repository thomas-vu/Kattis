h, w, _ = [int(x) for x in input().split()]
bricks = [int(x) for x in input().split()]

for _ in range(h):
    layer = 0

    while layer < w:
        if len(bricks) != 0:
            layer += bricks.pop(0)
        else:
            print("NO")
            raise SystemExit

    if layer > w:
        print("NO")
        raise SystemExit

print("YES")
