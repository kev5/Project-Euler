# Copyright 2018 Keval Khara kevalk@bu.edu

from math import sqrt


def primeSieve(sieveSize):
	'''Returns a list of prime numbers'''
	sieve = [True] * sieveSize
	# 0 and 1 are not prime
	sieve[0] = False
	sieve[1] = False

	# Create the sieve
	for i in range(2, int(sqrt(sieveSize)) + 1):
		pointer = i * 2
		while pointer < sieveSize:
			sieve[pointer] = False
			pointer += i

	# Compile the list of primes
	primes = []
	for i in range(sieveSize):
		if sieve[i] == True:
			primes.append(i)
	return primes

print(primeSieve(1000000))
