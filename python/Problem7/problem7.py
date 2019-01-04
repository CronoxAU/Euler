#Solution to Project Euler problem 7 - https://projecteuler.net/problem=7
#What is the 10 001st prime number

import math 
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from shared.prime import isPrime

#returns the n-th prime number
def getNthPrime(n):
  i = 0
  while n > 0:
    i += 1
    if isPrime(i):
      n = n - 1
  return i


#print(getNthPrime(10001))