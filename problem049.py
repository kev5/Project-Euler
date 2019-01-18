# Copyright 2018 Keval Khara kevalk@bu.edu

from itertools import permutations


def primeSieve(sieveSize):
	'''Returns a list of prime numbers'''
	sieve = [True] * sieveSize
	# 0 and 1 are not prime
	sieve[0] = False
	sieve[1] = False

	# Create the sieve
	for i in range(3, int(sieveSize ** 0.5) + 1, 2):
		pointer = i * 2
		while pointer < sieveSize:
			sieve[pointer] = False
			pointer += i

	# Compile the list of primes
	primes = []
	for i in range(3, sieveSize, 2):
		if sieve[i] == True:
			primes.append(i)

	return primes


# create the number
def create(b):
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            difference = b[j] - b[i]
            if b[j] + difference in b:
                return str(b[i])+str(b[j])+str(b[j]+difference)
    return False


# sieving prime numbers less than 10000
primes = primeSieve(10000)

# primes greater than 1487
primes = [x for x in primes if x > 1487]

# concatenate for the result
for i in primes:
    p = permutations(str(i))
    a = [int(''.join(x)) for x in p]
    a = list(set([x for x in a if x in primes]))
    a.sort()
    if len(a) >= 3:
        if create(a):
            print(create(a))
            break
