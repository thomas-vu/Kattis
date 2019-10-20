import math
D, V = [int(x) for x in input().split()]
Voriginal = math.pi * (D/2)**2 * D # pi * r^2 * h
print(Voriginal) # d = D
Vleftover = Voriginal-V
print(Vleftover)
#Vcone = math.pi * (D/2)**2 * (D/2) / 3 # pi * r^2 * h / 3
#print(Voriginal-2*Vcone)   # d = 0, chopped = max

#print(250/(Voriginal-2*Vcone))
#print(10*250/(Voriginal-2*Vcone))

#2 * (math.pi * h / 3 (R**2 + R*r + r**2)) + (math.pi * r**2 * h)
