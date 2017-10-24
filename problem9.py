# Copyright 2017 Keval Khara kevalk@bu.edu

import math
sum = 1000

for a in range(1,math.floor(sum/3)):
	for b in range(a,math.floor(sum/2)):
		c = sum - a - b

		if(a*a + b*b == c*c):
			print(str(a) + "*" + str(b) + "*" + str(c) + "=" + str(a*b*c))
