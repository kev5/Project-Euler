# Copyright 2018 Keval Khara kevalk@bu.edu
# Copyright 2018 Keval Khara kevalk@bu.edu

from itertools import permutations

# permutations of 0-9 pandigital
p = permutations('0123456789')

# variable to store the value of sum
solution = 0

# for loop to loop through permutations
for i in p:
    if (int(''.join(i[7:10])) % 17 == 0 and
        int(''.join(i[6:9])) % 13 == 0 and
        int(''.join(i[5:8])) % 11 == 0 and
        int(''.join(i[4:7])) % 7 == 0 and
        int(''.join(i[3:6])) % 5 == 0 and
        int(''.join(i[2:5])) % 3 == 0 and
        int(''.join(i[1:4])) % 2 == 0):
        solution += int(''.join(i))

print(solution)
