# Copyright 2017 Keval Khara kevalk@bu.edu

TOTAL = 200

# At the start of each loop iteration, ways[i] is the number of ways to use
# {any copies of the all the coin values seen before this iteration}
# to form an unordered sum of i

ways = [1] + [0] * TOTAL
for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
  for i in range(len(ways) - coin):
    ways[i + coin] += ways[i]

print(ways[-1])
