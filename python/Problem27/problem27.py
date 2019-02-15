# Solution to Project Euler problem 27 - https://projecteuler.net/problem=27
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

#check if the supplied number is prime
def isPrime(n):
    

def maxQuadraticPrimeFormular(limit):
    maxA = 0
    maxB = 0
    maxLength = 0
    for a in range(0-limit,limit):
        for b in range(0-limit,limit):
            currentLength = 0
            while isPrime((n * n) + (a * n) + b):
                currentLength += 1
            if(currentLength > maxLength):
                maxLength = currentLength
                maxA = a
                maxB = b
    return (maxA, maxB, maxLength)