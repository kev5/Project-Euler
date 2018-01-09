# Copyright 2018 Keval Khara kevalk@bu.edu

from math import sqrt

def pandigital_product(n):
	# Find and examine all factors of n
	for i in range(1, int(sqrt(n) + 1)):
		if n % i == 0:
			temp = str(n) + str(i) + str(n // i)
			if "".join(sorted(temp)) == "123456789":
				return True
	return False

ans = sum(num for num in range(1, 10000) if pandigital_product(num))
print(ans)
