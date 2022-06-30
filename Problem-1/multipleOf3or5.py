#!/usr/bin/python
def numThreeFive(n):
  sumTotal = 0
  for i in range(n):
    if i %  3 == 0 or i % 5 == 0:
      sumTotal += i
  return sumTotal
print(numThreeFive(100))