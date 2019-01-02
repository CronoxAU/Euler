#Solution to Project Euler problem 7 - https://projecteuler.net/problem=7
#What is the 10 001st prime number

import math 

def isPrime(num):
  if num <= 1: return False
  if num == 2: return True
  if num % 2 == 0: return False
  upperLimit = math.floor(math.sqrt(num))
  #we can increment i by 2 as every skipped value will be even and thus the %2 factor check above would have matched
  for i in range(3,upperLimit+1, 2):
      if num % i == 0:
        return False
  return True

#returns the n-th prime number
def getNthPrime(n):
  i = 0
  while n > 0:
    i += 1
    if isPrime(i):
      n = n - 1
  return i


#print(getNthPrime(10001))