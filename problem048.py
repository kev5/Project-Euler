# Copyright 2018 Keval Khara kevalk@bu.edu

L = 1000    
d = 10**10
res = sum(pow(n, n) for n in range(1, L+1)) 

print(res % d)   # because we only want last 10 digits
