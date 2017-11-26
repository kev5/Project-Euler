# Copyright 2017 Keval Khara kevalk@bu.edu

limit = 28124
divisor_sum = [0] * limit
for i in range(1, limit):
	for j in range(i * 2, limit, i):
		divisor_sum[j] += i
abundant_nums = [i for (i, x) in enumerate(divisor_sum) if x > i]

is_abundant = [False] * limit
for i in abundant_nums:
	for j in abundant_nums:
		if i + j < limit:
			is_abundant[i + j] = True
		else:
			break

# Sum of all the integers which cannot be written as sum of 2 abundant numbers
ans = sum(i for (i, x) in enumerate(is_abundant) if not x)

print(ans)
