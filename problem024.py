# Copyright 2017 Keval Khara kevalk@bu.edu

from itertools import permutations

lexi_perm = list(permutations('0123456789'))

# Each permutation is in the form of tuple
# so joining all the strings 
ans = ''.join(lexi_perm[999999])

print(ans)
