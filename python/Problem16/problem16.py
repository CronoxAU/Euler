#Solution to Project Euler problem 16 - https://projecteuler.net/problem=16
#What is the sum of the digits of the number 21000?

#returns the sum of the digits in n
def sumDigits(n):
  sum = 0
  # work through each digit, starting at the right
  while n > 0:
    sum += n %10
    n //= 10
  return sum
