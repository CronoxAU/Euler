#Solution to Project Euler problem 1 - https://projecteuler.net/problem=1
#Find the sum of all the multiples of 3 or 5 below 1000.

def uniqueSumOfTwoMultiples(x, y, upperLimit):
  return sumMultiples(x, upperLimit) + sumMultiples(y, upperLimit) - sumMultiples(x * y, upperLimit)

def sumMultiples(x, upperLimit):
  sum = 0
  if x > 0 and upperLimit > 0 and x < upperLimit:
    for i in range(x,upperLimit,x):
      sum = sum + i
  return sum

#result = uniqueSumOfTwoMultiples(3,5,1000)
#print(result)