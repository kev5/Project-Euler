# Copyright 2017 Keval Khara kevalk@bu.edu 

import math

print(3 * (math.floor(999/3) * (math.floor(999/3)+1))/2
+ 5 * (math.floor(999/5) * (math.floor(999/5)+1))/2
-15 * (math.floor(999/15) * (math.floor(999/15)+1))/2)

'''
Since the sum of natural numbers from 1 to n is (n*(n+1))/2,
Thus the sequences for any number divisible by n can be written as n*N*(N+1)/2,
where N = highest number divisible by n less than the highest number of the sequence

This solution has a time complexity of O(1) which is better than O(n) which we get 
when we have a loop going through the entire sequence
'''
