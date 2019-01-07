#Solution to Project Euler problem 12 - https://projecteuler.net/problem=12
#What is the value of the first triangle number to have over five hundred divisors?
import math 

#Returns the number of divisors of the supplied num
def getNumberOfDivisors(num):
  divisorsCount = 0
  sqrRoot = int(math.sqrt(num))
  for i in range(i,int(sqrRoot)):
    if num % i = 0:
      if i == sqrRoot:
        divisorsCount += 1
      else:
        #Add 2 to the count if this is not the square root, to factor in the larger factor.
        divisorsCount += 2
  return divisorsCount

def getTriangleNumberByDivisorCount(divisorCount):
  resultFound = False
  triangleNumber = 1
  while not resultFound
    if getNumberOfDivisors(triangleNumber) >= divisorCount
      resultFound = True
  return triangleNumber

