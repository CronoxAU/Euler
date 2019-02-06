#Solution to Project Euler problem 20 - https://projecteuler.net/problem=20
#Find the sum of the digits in the number 100!


#returns the sum of the digits in the supplied number n
def sumOfDigits(n):
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  return sum