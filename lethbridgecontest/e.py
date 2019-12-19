k = int(input())
a = bin(k)[2:]
print(a)
for i in reversed(a):
    if i == '0':
        print('AddRockets')
    else:
        print('Go')
        print('AddRockets')
