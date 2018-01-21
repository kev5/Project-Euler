# Copyright 2018 Keval Khara kevalk@bu.edu

ans = 0

for i in range(1,10000):
	multiplication = ''
	integer = 1    # (1,2,.....n)

	while len(multiplication) < 9:
		multiplication += str(i*integer)
		integer += 1

	if ((len(multiplication) == 9) and (len(set(multiplication)) == 9) 
		and ('0' not in multiplication)):
		if int(multiplication) > ans:
			ans = int(multiplication)

print(ans)
