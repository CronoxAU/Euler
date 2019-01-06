#Solution to Project Euler problem 10 - https://projecteuler.net/problem=10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.
import math 
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from shared.prime import isPrime

#returns the product of each digit in the string str
def getSumOfPrimes(upperLimit):
  sum = 0
  for i in range(2,upperLimit):
    if isPrime(i):
      sum += i
  return sum

