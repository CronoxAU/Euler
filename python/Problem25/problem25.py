# Solution to Project Euler problem 25 - https://projecteuler.net/problem=25
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# Brute force approch
# Generate each number in the Fibonacci sequence until we reach one with the required number of digits

# Retuns the index of the first number in the Fibonacci sequence with n digits
def indexOfFirstFibonacciWithNDigits(n):
    #special case for 1 digit, just return 1
    if n == 1:
        return n
    currentF = 1
    previousF = 1
    i = 2
    while i > 0:
        if(len(str(currentF)) >= n):
            return i
        temp = currentF
        currentF = previousF + currentF
        previousF = temp
        i += 1



