# Copyright 2017 Keval Khara kevalk@bu.edu

def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b,a%b)

ans = 1
for i in range(1, 21):
	ans *= i / gcd(i, ans)
print(ans)
