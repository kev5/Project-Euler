# Copyright 2018 Keval Khara kevalk@bu.edu

T = set((n * (n + 1) / 2) for n in range(2, 200000))
P = set((n * ((3 * n) - 1) / 2) for n in range(2, 200000))
H = set((n * ((2 * n) - 1)) for n in range(2, 200000))
for i in T:
    if i in P and i in H:
        print(i)
    else:
        continue
