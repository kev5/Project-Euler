# Copyright 2017 Keval Khara kevalk@bu.edu

'''
*21* 22 23 24 *25*
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
*17* 16 15 14 *13*
From the diagram, let's observe the four corners of an n * n square (where n is odd).
It's not hard to convince yourself that the top right corner always has the value n^2.
Working counterclockwise (backwards), the top left corner has the value n^2 - (n - 1),
the bottom left corner has the value n^2 - 2(n - 1), and the bottom right is n^2 - 3(n - 1).
Putting it all together, this outermost ring contributes 4n^2 - 6(n - 1) to the final sum.
'''

