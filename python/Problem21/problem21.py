#Solution to Project Euler problem 21 - https://projecteuler.net/problem=21
#Evaluate the sum of all the amicable numbers under 10000.

#returns the sum of the factors of the supplied number n
def sumOfFactors(n):
  sum = 0
  for i in range(1,(n+1)//2):
    if n % i == 0:
      sum += i
  return sum

#if n is an amicable number it's pair is returned, otherwise 0 is returned
def getAmicablePair(n):
  #get the sum of the factors of n, this is the potential pair
  result = 0
  potentialPair = sumOfFactors(n)
  #get the sum of the factors of the potential pair, if this equals n we have found an amicable pair, return the potential pair value
  #otherwise return 0
  if sumOfFactors(potentialPair) == n:
    result = potentialPair
  return result

#returns the sum of all amicable numbers below the limit
def sumAmicableNumbers(limit):
  sum = 0
  #loop through each number, if it is amicable, add it to the sum
  for i in range(1,limit):
    if getAmicablePair(i) > 0:
      sum += i
  return sum