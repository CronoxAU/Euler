#Solution to Project Euler problem 3 - https://projecteuler.net/problem=3
#What is the largest prime factor of the number 600851475143.
import math 

def isPrime(num):
  if num <= 1: return False
  if num % 2 == 0: return False
  upperLimit = math.floor(math.sqrt(num))
  #we can increment i by 2 as every skipped value will be even and thus the %2 factor check above would have matched
  for i in range(3,upperLimit+1, 2):
      if num % i == 0:
        return False
  return True

def largestPrimeFactor(num):
  largestPrimeFactor = 0
  upperLimit = math.floor(math.sqrt(num))
  for i in range(upperLimit, 0, -1):
    if num % i == 0:
      if i > largestPrimeFactor:
        if isPrime(i):
          largestPrimeFactor = i
      #check the other half of the factor
      j = num / i
      if j > largestPrimeFactor:
        if isPrime(j):
          largestPrimeFactor = j
  return largestPrimeFactor

result = largestPrimeFactor(600851475143)
print(result)