# Copyright 2018 Keval Khara kevalk@bu.edu

# Copyright 2018 Keval Khara kevalk@bu.edu

from math import factorial as fact


f = [fact(0),
fact(1),
fact(2),
fact(3),
fact(4),
fact(5),
fact(6),
fact(7),
fact(8),
fact(9)]


def factorial_digits(n):
	digit = 0
	while n:
		digit += f[n%10]
		n //= 10
	return digit

ans = 0

for i in range(10,1000000):
	if factorial_digits(i) == i:
		ans += i

print(ans)
