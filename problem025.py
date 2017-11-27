# Copyright 2017 Keval Khara kevalk@bu.edu

fib = [0,1]

i = 2

while True:
	fib_new = fib[i-1]+fib[i-2]
	fib.append(fib_new)

	if fib_new > (10**999):
		print(i)
		break
	i = i+1
