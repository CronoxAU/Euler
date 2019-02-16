# Solution to Project Euler problem 27 - https://projecteuler.net/problem=27
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

import math

#use prime mask to store the results of primes and non-primes we have already calculated
primeMask = []

# check if the supplied number is prime
# use the prime mask list to record results and speed up processing
def isPrime(n):
    global primeMask
    if primeMask[n] == 1: return True
    if primeMask[n] == 0: return False
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    upperLimit = math.floor(math.sqrt(n))
    #we can increment i by 2 as every skipped value will be even and thus the %2 factor check above would have matched
    for i in range(3,upperLimit+1, 2):
        if n % i == 0:
            primeMask[n] = 0
            return False
    primeMask[n] = 1
    return True

# find the quadratic equation in the form n² + an + b, where n starts at 0, that produces the longest sequence of prime numbers
# limit specifies the search range for both a and b, starting at both -limit and going to limit.
def maxQuadraticPrimeFormular(limit):
    global primeMask
    primeMask = [-1] * ((limit * limit) + (limit * limit) + (limit))
    maxA = 0
    maxB = 0
    maxLength = 0
    for a in range(0-limit,limit):
        for b in range(0-limit,limit):
            currentLength = 0
            n = 0
            absN = abs(n)
            while isPrime((absN * absN) + (a * absN) + b):
                currentLength += 1
                n += 1
                absN = abs(n)
            if(currentLength > maxLength):
                maxLength = currentLength
                maxA = a
                maxB = b
    return (maxA, maxB, maxLength)

# finds the product of a and b from the quadratic equation in the form n² + an + b, that produces the longest sequence of prime numbers
def maxQuadraticPrimeProduct(limit):
    result = maxQuadraticPrimeFormular(1000)
    return result[0] * result[1]