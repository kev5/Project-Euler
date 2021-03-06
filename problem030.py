# Copyright 2017 Keval Khara kevalk@bu.edu

def digit_fifth_powers_sum(n):
	return sum(int(c)**5 for c in str(n))

res = sum(i for i in range(2, 1000000) if i == digit_fifth_powers_sum(i))
print(res)
