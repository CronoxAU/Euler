#Solution to Project Euler problem 12 - https://projecteuler.net/problem=12
#What is the value of the first triangle number to have over five hundred divisors?
import math 

#Returns the number of divisors of the supplied num
def getNumberOfDivisors(num):
  divisorsCount = 0
  sqrRoot = math.sqrt(num)
  for i in range(1,int(sqrRoot)+1):
    if num % i == 0:
      if i == sqrRoot:
        divisorsCount += 1
      else:
        #Add 2 to the count if this is not the square root, to factor in the larger factor.
        divisorsCount += 2
  return divisorsCount

def getLowestTriangleNumberByNoOfDivisors(NoOfDivisors):
  resultFound = False
  triangleNumber = 1
  i =  1
  while not resultFound:
    i += 1
    if getNumberOfDivisors(triangleNumber) >= NoOfDivisors:
      resultFound = True
    else:
      triangleNumber += i
  return triangleNumber

