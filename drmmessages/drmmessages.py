import string
ABC = string.ascii_uppercase

def rotate(c, rot):
    return ABC[(ABC.index(c) + rot) % 26]

message = input()
half = len(message) // 2

first_half = message[:half]
second_half = message[half:]

rot1 = sum(ABC.index(c) for c in first_half)
rot2 = sum(ABC.index(c) for c in second_half)

rotated1 = [rotate(c, rot1) for c in first_half]
rotated2 = [rotate(c, rot2) for c in second_half]

decrypted = [rotate(c, ABC.index(r)) for c, r in zip(rotated1, rotated2)]
print("".join(decrypted))
