#Solution to Project Euler problem 6 - https://projecteuler.net/problem=6
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

import math

#returns the sum of the squares of all positive numbers, starting at 1 and ending at the supplied num (inclusive)
def sumOfSquares(num):
  sum = 0
  for i in range(1, num+1):
    sum += i*i
  return sum

#returns the square of the sum of all positive numbers, starting at 1 and ending at the supplied num (inclusive)
def squareOfSums(num):
  sum = 0
  for i in range(1, num+1):
    sum += i
  return sum * sum

def diffBetweenSquareOfSumsAndSumOfSquares(num):
  return squareOfSums(num) - sumOfSquares(num)


print(diffBetweenSquareOfSumsAndSumOfSquares(100))