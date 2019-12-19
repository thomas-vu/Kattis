import string
S = input()
K = int(input())

S = ''.join(S.split('-')).upper()
rem = len(S) % K
front = S[:rem]
back = S[rem:]
dashed = [back[i:i+K] for i in range(0, len(back), K)]
if front != '':
    dashed.insert(0, front)
print('-'.join(dashed))
