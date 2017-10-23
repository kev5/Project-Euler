# Copyright 2017 Keval Khara kevalk@bu.edu

def nth_prime(n, limit=125000):
    if limit % 2 != 0: limit += 1
    primes = [True] * limit
    primes[0],primes[1] = [None] * 2
    count = 0 	#number of primes
    for i,val in enumerate(primes):
        if val is True:
            # sieve out non-primes by multiples of known primes
            primes[i*2::i] = [False] * (((limit - 1)//i) - 1)
            count += 1
        if count == n: return i
    return False

prime = nth_prime(10001)
print(prime)
