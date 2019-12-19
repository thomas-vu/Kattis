# Python program to print prime factors
import math
 
# A function to print all prime factors of 
# a given number n
def primeFactors(n):
     
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2, end=' ')
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            print(i, end=' '),
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)

#primeFactors(int(input()))

#======================================================

k = 0
n = int(input())
while n % 2 == 0:
    k += 1
    n = n / 2
     
for i in range(3, int(math.sqrt(n))+1, 2):
    while n % i == 0:
        k += 1
        n = n / i
         
if n > 2:
    print(1)
else:
    print(k)
