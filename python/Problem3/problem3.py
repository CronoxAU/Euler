#Solution to Project Euler problem 3 - https://projecteuler.net/problem=3
#What is the largest prime factor of the number 600851475143.
import math 
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from shared.prime import isPrime

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

#result = largestPrimeFactor(600851475143)
#print(result)