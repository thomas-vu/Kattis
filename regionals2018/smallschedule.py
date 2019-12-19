Q, M, S, L = [int(i) for i in input().split()]
Srem = S
Lrem = L
total = 0
while (Srem != 0 or Lrem != 0):
    if M <= Lrem:
        Lrem = max(0, Lrem - M)
        total += Q
    else:
        if Lrem == 0:
            Srem = max(0, Srem - M)
            total += 1
        else:
            Mrem = M - Lrem
            Lrem = 0
            Srem = max(0, Srem - (Q * Mrem))
            total += Q
    if Srem == 0 and Lrem == 0:
        break

print(total)
