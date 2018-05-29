# Copyright 2017 Keval Khara kevalk@bu.edu

from math import sqrt
score = lambda word: sum(ord(c)-64 for c in word)
is_tri_num = lambda t: (sqrt(1 + 8*t) - 1) / 2 % 1 == 0

print(sum(is_tri_num(score(x[1:-1])) for x in open('p042_words.txt').read().split(',')))
