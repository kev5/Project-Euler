# Copyright 2018 Keval Khara kevalk@bu.edu

'''
We use regular expressions to increase the efficiency of
our code since the numbers with even digits can be
skipped as we know they won't be prime while truncating
the digits
'''

import re
from math import sqrt


def is_prime(n):
    '''Check if the number is prime'''
    n = int(n)
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2==0 or n%3 == 0:
        return False
    f = 5
    while f <= int(sqrt(n)):
        if n%f == 0 or n%(f+2) == 0:
            return False
        f+= 6
    return True


def is_trunc(n):
    '''Check if the truncated numbers are prime'''
    for d in range(1, len(str(n))):
        if not is_prime(str(n)[d:]) or not is_prime(str(n)[:d]): 
            return False 
    return True


n = 11
f = 1
ans = []
while len(ans) < 11:
    n += 3-f    # fast count for primes
    f = -f
    if not (n > 100 and re.search('[245680]', str(n))):
        if is_prime(n) and is_trunc(n):
            ans.append(n)
print(sum(ans))
