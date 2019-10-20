from collections import Counter

def is_permutation(a, b):
    return Counter(a) == Counter(b)

def clean(pattern):
    return filter(lambda x: x.isalpha(), pattern).lower()

while True:
    try:
        a, b = input()
        print('Valid Pattern' if is_permutation(clean(a), clean(b)) else 'Invalid Pattern')
    except:
        break
