# Copyright 2018 Keval Khara kevalk@bu.edu

# Copyright 2018 Keval Khara kevalk@bu.edu

def is_pandigital(n, s=9):
	n=str(n)
	return len(n)==s and not '1234567890'[:s].strip(n)


def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n%2==0 or n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0: return False
        f+= 6
    return True

n = 7654321

while not(is_pandigital(n, 7) and is_prime(n)): n-= 2

print(n)
