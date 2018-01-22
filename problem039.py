# Copyright 2018 Keval Khara kevalk@bu.edu

from collections import Counter

perimeters = []

for a in range(1, 500):
    for b in range(a, 500):
        c = (a**2 + b**2)**0.5
        if int(c) == c and a + b + c <= 1000:
            perimeters.append(a+b+c)

# Counting the instances of perimeters
p = Counter(perimeters)

# Printing the most repeated perimeter
print(p.most_common(1)[0])
