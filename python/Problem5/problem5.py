#Solution to Project Euler problem 5 - https://projecteuler.net/problem=5
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.
#While this solution works, and is generic, it is very slow. I would like to look for a better way to implement this.

import math

#returns true if the supplied num is evenly divisible by all numbers up to and including the specified upperLimit
def isEvenlyDivisibleByAll(num, upperLimit):
  #onlyneed  test the upper half of numbers below the upper limit
  for i in range(math.floor(upperLimit/2), upperLimit+1):
    if(num % i ):
      return False
  return True


#returns the lowest positive number evenly divisible by all numbers up to and including the specified upperLimit
def lowestEvenlyDivisibleByAll(upperLimit):
  result = 0
  i = upperLimit
  while result == 0:
    if(isEvenlyDivisibleByAll(i, upperLimit)):
      result = i
    #increment by the upper limit, as the number must be divisible by this limit
    i += upperLimit
  return result


print(lowestEvenlyDivisibleByAll(20))