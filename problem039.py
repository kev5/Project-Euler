# Copyright 2018 Keval Khara kevalk@bu.edu

'''
We know that the value of c can be written as √a2+b2. So the perimeter can be written as:
p = a + b + c
⇒p = a + b + √a2+b2

Now if we will consider b = 0 then
⇒p = a + 0 + a
⇒p = 2a
So 2a ≤ 1000
a ≤ 500
Similarly, b ≤ 500.
'''

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
