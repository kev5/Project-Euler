# Copyright 2017 Keval Khara kevalk@bu.edu

import eulerlib
from itertools import count


def count_primes(ab):
	a, b = ab
	for i in count():
		n = (i * i) + (i * a) + b
		if not is_prime(n):
			return i


isprime = eulerlib.primes(1000)		# Get a list of all primes less than 1000


def is_prime(n):
	if n < 0:
		return False
	elif n < len(isprime):
		return isprime[n]
	else:
		return eulerlib.is_prime(n)


ans = max(((a, b) for a in range(-999, 1000) for b in range(2, 1000)),
		key=count_primes)
print(str(ans[0] * ans[1]))
