# Copyright 2017 Keval Khara kevalk@bu.edu

def prime_sum(n):
    if n % 2 != 0: n += 1
    primes = [True] * n
    primes[0],primes[1] = [None] * 2
    sum = 0
    count = 0 	#number of primes
    for i,val in enumerate(primes):
        if val is True:
            # sieve out non-primes by multiples of known primes
            primes[i*2::i] = [False] * (((n - 1)//i) - 1)
            count += 1
            sum += i    
    return sum

prime = prime_sum(2000000)
print(prime)
