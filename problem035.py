# Copyright 2018 Keval Khara kevalk@bu.edu
# Copyright 2018 Keval Khara kevalk@bu.edu

import math


def primeSieve(n):
    '''Get all primes below n with the sieve of Eratosthenes'''
    from math import ceil
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    primeList = []
    roundUp = lambda n, prime: int(ceil(float(n) / prime))
    for currentPrime in range(2, n):
        if not primes[currentPrime]:
            continue
        primeList.append(currentPrime)
        for multiplicant in range(2, roundUp(n, currentPrime)):
            primes[multiplicant * currentPrime] = False
    return primes


def isCircularPrime(primes, number):
    '''Check if the number is a circular prime'''
    number = str(number)
    for i in range(len(number)):
        rotatedNumber = number[i:] + number[:i]
        if not primes[int(rotatedNumber)]:
            return False
    return True


if __name__ == "__main__":
    primes = primeSieve(1000000)
    ans = 0
    for prime, isPrime in enumerate(primes):
        if not isPrime:
            continue
        if isCircularPrime(primes, prime):
            ans += 1

    print(ans)
