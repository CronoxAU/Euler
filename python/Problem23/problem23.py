#Solution to Project Euler problem 23 - https://projecteuler.net/problem=23
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

#returns the sum of the factors of the supplied number n
def sumOfFactors(n):
  sum = 0
  for i in range(1,n//2+1):
    if n % i == 0:
      sum += i
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
      abList.push(i)
  return abList

#returns true is n is the sum of two digits in the supplied list
def isSumFromList(n,list):
  list.sort()
  for i in range (0,len(list)):
    for j in range (0,len(list)):
      if list[i] + list[j] == n:
        return True
      j =+ 1
      if list[j] > n:
        break
    i =+ 1
    if list[i] > n:
      break

# Returns the sum of all the positive integers below the supplied limit which cannot be written as the sum of two abundant numbers.
# As all numbers above 28123 can be written as the sum of an abundant number, any limit higher than this will return the same result
def fullSolution(limit):
  result = 0
  if limit > 28123:
    limit = 28123
  abList = generateAbundantList(limit)
  for i in range(1,limit+1):
    if not isSumFromList(i,abList):
      result += i
  return result