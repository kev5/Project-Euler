# Copyright 2017 Keval Khara kevalk@bu.edu

from itertools import count

def reciprocal_cycle(n):
	res = {}
	x = 1
	for d in count():
		if x in res:
			return d - res[x]
		else:
			res[x] = d
			x = x * 10 % n

ans = max(range(1,1000), key = reciprocal_cycle)
print(ans)
