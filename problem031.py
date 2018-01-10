# Copyright 2018 Keval Khara kevalk@bu.edu

SUM = 200

# At the start of each loop iteration, ways[i] is
# the number of ways to use any copies of all
# the coin values seen before this iteration
# to form an unordered sum of i

ways = [1] + [0] * SUM
coins = [1, 2, 5, 10, 20, 50, 100, 200]
for coin in coins:
  for i in range(len(ways) - coin):
    ways[i + coin] += ways[i]

print(ways[-1])
