# Copyright 2018 Keval Khara kevalk@bu.edu

from fractions import gcd

'''
 Let num = 10 * n1 + n0 be the numerator.
 Let den = 10 * d1 + d0 be the denominator.
 
 As stated in the problem, we need 10 <= n < d < 100.
 Also, we must disregard trivial simplifications where n0 = d0 = 0.
'''

num = 1
den = 1
for d in range(10, 100):
	for n in range(10, d):
		n0 = n % 10
		n1 = n // 10
		d0 = d % 10
		d1 = d // 10
		if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
			num *= n
			den *= d

print(den // gcd(num, den))
