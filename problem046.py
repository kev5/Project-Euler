# Copyright 2018 Keval Khara kevalk@bu.edu

from math import sqrt


def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n)+1),2):
            if n % i == 0:
                return False
        return True

n = 3
primes = [2]

while True:
    if is_prime(n):
        primes.append(n)
    else:
        for i in primes:
            if sqrt(((n-i)/2)) == int(sqrt(((n-i)/2))):
                break
        else:
            print(n)
            break
    n += 2
 
