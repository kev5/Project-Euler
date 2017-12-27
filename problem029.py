# Copyright 2017 Keval Khara kevalk@bu.edu

'''
A set is the best way to store values when we do not want
any duplicate values in our result
'''

result = set(a**b for a in range(2, 101) for b in range(2, 101))
print(len(result))
