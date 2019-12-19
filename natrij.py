now = [int(x) for x in input().split(':')]
future = [int(x) for x in input().split(':')]
now = now[0] * 3600 + now[1] * 60 + now[2]
future = future[0] * 3600 + future[1] * 60 + future[2]

S = (future-now if now < future else 86400-now+future)
H = S // 3600
S -= H * 3600
M = S // 60
S -= M * 60

H, M, S = str(H), str(M), str(S)
if len(H) == 1:
    H = '0' + H
if len(M) == 1:
    M = '0' + M
if len(S) == 1:
    S = '0' + S

print('{}:{}:{}'.format(H, M, S))
