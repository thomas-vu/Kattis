import string
ABC = string.ascii_uppercase
def rotate(c, rot):
    return ABC[(ABC.index(c) + rot) % 26]
m = input()
print("".join([rotate(c, ABC.index(r)) for c, r in zip([rotate(c, sum(ABC.index(c) for c in m[:len(m) // 2])) for c in m[:len(m) // 2]], [rotate(c, sum(ABC.index(c) for c in m[len(m) // 2:])) for c in m[len(m) // 2:]])]))
