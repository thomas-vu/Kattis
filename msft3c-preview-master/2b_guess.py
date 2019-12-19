from collections import Counter

def is_consistent(guess, gp, gc, actual):
    g = Counter(guess)
    a = Counter(actual)
    p = 0
    for i in range(3):
        if guess[i] == actual[i]:
            p += 1
            g[guess[i]] -= 1
            a[actual[i]] -= 1
    if gp != p:
        return False
    return gc == sum((g & a).values())

def solve(test):
    guess1 = test[:3]
    guess1p = int(test[3])
    guess1c = int(test[4])
    guess2 = test[6:9]
    guess2p = int(test[9])
    guess2c = int(test[10])
    n = 0
    result = None
    for a in 'RGB':
        for b in 'RGB':
            for c in 'RGB':
                test = a + b + c
                if is_consistent(guess1, guess1p, guess1c, test) and \
                   is_consistent(guess2, guess2p, guess2c, test):
                    n += 1
                    result = test
    if not result:
        result = 'Blue Screen: A problem has been detected'
    elif n != 1:
        result = 'Download and install updates for your input'
    return result

while True:
    try:
        print(solve(raw_input()))
    except:
        break
