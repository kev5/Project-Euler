# Copyright 2017 Keval Khara kevalk@bu.edu

limit = 1000000
collatz_length = [0] * limit
collatz_length[1] = 1
max_length = [1,1]
 
for i in range(1,1000000):
    n,s = i,0
    TO_ADD = []       # collatz_length not yet known
    while n > limit - 1 or collatz_length[int(n)] < 1:
        TO_ADD.append(n)
        if n % 2 == 0: n = n/2
        else: n = 3*n + 1
        s += 1
    # collatz_length now known from previous calculations
    p = collatz_length[int(n)]
    for j in range(s):
        m = TO_ADD[j]
        if m < limit:
            new_length = collatz_length[int(n)] + s - j
            collatz_length[int(m)] = new_length
            if new_length > max_length[1]: max_length = [i,new_length]
print(max_length[0])
