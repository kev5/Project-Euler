# Copyright 2017 Keval Khara kevalk@bu.edu

def pow2sum(exp):
    pow = list(str(2**1000))
    return sum([int(i) for i in pow])
 
print(pow2sum(1000))
