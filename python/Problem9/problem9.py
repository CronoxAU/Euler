#Solution to Project Euler problem 9 - https://projecteuler.net/problem=9
#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

import math 

#returns the product of each digit in the string str
def isPythagoreanTriplet(a,b,c):
  result = False
  if a < b and b < c:
    if (a*a) + (b*b) == (c*c):
      result = True
  return result

def getProductOfPythagoreanTripletBySum(sum):
  #search through each possible a and b to find a matching result
  for a in range(1,int(sum/3)):
    for b in range(2,int(sum/2)):
      c = sum - a - b
      if isPythagoreanTriplet(a,b,c):
        return a * b * c
  return 0

