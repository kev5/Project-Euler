# Copyright 2017 Keval Khara kevalk@bu.edu

n = 600851475143
i = 2
while i * i <= n:
    if i * i == n:
        n = i
        break

    while n%i == 0:
        n = n / i
    i = i + 1

print (n)
