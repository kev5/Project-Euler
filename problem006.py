# Copyright 2017 Keval Khara kevalk@bu.edu

n=100

#sum of the first n natural numbers
s=sum(i for i in range(1,n+1))

#sum of the squares of the first n natural numbers
s2=sum(i*i for i in range(1,n+1))

print((s*s) - s2)
