# Copyright 2017 Keval Khara kevalk@bu.edu

sum=0
n1=1
n2=2
while (n1<=4000000):
	if (n1%2 == 0):
		sum += n1
	n1=n2
	n2=n1+n2
print(sum)
