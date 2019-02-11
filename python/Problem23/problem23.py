#Solution to Project Euler problem 23 - https://projecteuler.net/problem=23
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

#METHOD
# create a list of all abundant numbers below the limit
# Use this list to create a list of all the sums of abundant numbers below the limit
# Calculate the sum of all numbers in the list, this is the inverse of the needed solution (ie the sum of all numbers which can be written as the sum of two abundant numbers)
# Calculate the sum of all numbers below the limit
# Subreact the first sum from the second to get the needed solution

import math


# Returns the sum of all the positive integers below the supplied limit which cannot be written as the sum of two abundant numbers.
# As all numbers above 28123 can be written as the sum of an abundant number, any limit higher than this will return the same result
def sumOfNonAbundantSums(limit):
  if limit > 28123:
    limit = 28123
  abList = generateAbundantList(limit)
  listOfSums = generateListOfSums(abList, limit)
  sumOfAbundantSums = sumList(listOfSums)
  triangleNum = triangleNumber(limit)
  return triangleNum - sumOfAbundantSums

#returns the sum of the factors of the supplied number n
def sumOfFactors(n):
  if n == 1:
    return 1
  sum = 1
  sqrtOfN = int(math.sqrt(n))
  #if n is a perfect square, include that as a factor
  if(n == sqrtOfN * sqrtOfN):
    sum += sqrtOfN
    sqrtOfN -= 2
  for i in range(2,sqrtOfN+1):
    if n % i == 0:
      sum += i + (n//i)
  return sum

#if n is an abundant number true, otherwise false is returned
def isAbundant(n):
  result = False
  if sumOfFactors(n) > n:
    result = True
  return result

#returns a list of all abundant numbers below the supplied limit
def generateAbundantList(limit):
  abList = []
  for i in range(1,limit+1):
    if isAbundant(i):
      abList.append(i)
  return abList

#generates a deduplicated, sorted list of all possible numbers, below the supplied limit, created by adding two elements from the supplied list
def generateListOfSums(list, limit):
  result = []
  for i in range (0,len(list)):
    for j in range (0,len(list)):
      if(list[i]+list[j]) <= limit:
        result.append(list[i]+list[j])
      else:
        break
  result = deduplicateList(result)
  result.sort()
  return result

# deduplicates the provided list
def deduplicateList(list):
  result = []
  for i in list:
    if i not in result:
      result.append(i)
  return result

# Returns the sum of all items in the list
def sumList(list):
  result = 0
  for i in list:
    result += i
  return result

# returns the n-th triangle number, ie the sum of all numbers up to and including n
def triangleNumber(n):
  return (n*n + n)//2

  #returns true is n is the sum of two digits in the supplied list
# NOTE - this function only works on a sorted list, this was implemented for optimization.
# No longer used in current solution
def isSumFromList(n,list):
  #list.sort()
  for i in range (0,len(list)):
    for j in range (0,len(list)):
      if list[i] + list[j] == n:
        return True
      if list[j] > n:
        break
    if list[i] > n:
      break
  # if no match was found return false
  return False

