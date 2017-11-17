# Copyright 2017 Keval Khara kevalk@bu.edu


def factorial(n):
    if n == 0: return 1
    else: return n * factorial(n - 1)
 

def sum_digits(n):
    return sum([int(i) for i in str(n)])
 
sum = sum_digits(factorial(100))

print(sum)

'''
We can also write a 2-line code for this problem:

from math import factorial
print(sum(int(c) for c in str(factorial(100))))

'''
