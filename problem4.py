# Copyright 2017 Keval Khara kevalk@bu.edu

def pal(x):
    return int(str(x)[::-1]) == x

maxpal = 0
for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        prod = a * b
        if pal(prod) and prod > maxpal:
            maxpal = prod

print(maxpal)
