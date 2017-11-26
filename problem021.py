# Copyright 2017 Keval Khara kevalk@bu.edu

# Calculate the sum of proper divisors for each number
limit = [0] * 10000
for i in range(1, len(limit)):
	for j in range(i * 2, len(limit), i):
		limit[j] += i

# Find all amicable pairs within specified range
ans = 0
for i in range(1, len(limit)):
	j = limit[i]
	if j != i and j < len(limit) and limit[j] == i:
		ans += i
print(ans)
