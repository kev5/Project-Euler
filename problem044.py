# Copyright 2018 Keval Khara kevalk@bu.edu

from math import sqrt


def isPentagonal(number):
    penTest = (sqrt(1 + 24 * number) + 1.0) / 6.0
    return penTest == int(penTest)

result = 0
notFound = True
i = 1
 
while (notFound):
    i += 1
    n = i * (3 * i - 1) / 2
    for j in range (i-1, 0, -1):
        m = j * (3 * j - 1) / 2
        if (isPentagonal(n - m) and isPentagonal(n + m)):
            result = n - m
            notFound = False
            break

print("k =", i)
print("j =", j)
print("D =", result)
