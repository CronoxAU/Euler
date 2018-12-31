#Solution to Project Euler problem 4 - https://projecteuler.net/problem=4
#Find the largest palindrome made from the product of two 3-digit numbers.
import math

#Checks if the number supplied is a palindrome - This function is no longer used in this solution
def isPalindrome(num):
  original = str(num)
  reverse = original[::-1]
  if(original == reverse):
    return True
  return False

#Returns an integer palindrome using the prefix supplied as the starting digits
def makePalindrome(prefix):
  prefixString = str(prefix)
  suffixString = prefixString[::-1]
  fullString = prefixString + suffixString
  return int(fullString)

#returns the first half of the digits of the supplied number
def getFirstHalf(num):
  numString = str(num)
  mid= math.floor((len(numString) + 1) / 2)
  return int(numString[:mid])

#checks if the supplied num is the product of 2 three digit numbers
def isProductOfTwo3DigitNumbers(num):
  upperLimit = math.floor(math.sqrt(num))
  if upperLimit > 1000 or upperLimit < 100:
    return False
  for i in range(upperLimit, 100, -1):
    if num % i == 0:
      j = int(num / i)
      if j >= 100 and j < 1000:
        if num % j == 0:
          return True
  return False

#finds the largest palindromic number, which is a product of two 3 digit numbers, below the supplied upper limit
#returns 0 if no such number can be found
def findLargestPalindromeProductOfTwo3DigitNumbers(upperLimit):
  found = False
  #split the upper limit in half
  initialFirstHalf = getFirstHalf(upperLimit)
  # loop through each possible first half of a number above 100 (ie the first half of 100001 the smallest palindromic product of two 3 digit numbers)
  #start that the largest numbers first and decrement through, this way the first one found will be the largest.
  for i in range(initialFirstHalf, 100, -1):
    #create a palindrome using the first half as a root
    currentPalindrome = makePalindrome(i)
    #check if this palindrome is a product two 3 digit numbers. If it is the result has been found.
    if isProductOfTwo3DigitNumbers(currentPalindrome):
      return currentPalindrome

  return 0

print(findLargestPalindromeProductOfTwo3DigitNumbers(999*999))