# Solution to Project Euler problem 28 - https://projecteuler.net/problem=28
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# returns the sum of the diagonals of an n by n spiral
def sumOfSpiralDiagonals(n):
    sum = 1
    currentValue = 1
    # due to the shape of the spiral n must be odd to be valid
    if n%2 == 0:
        return 0
    # loop through the fomation, adding each diagonal
    for x in range(3, n+1, 2):
        # calculate the 4 corners of the current spiral and add each to the sum.
        for y in range(1, 5):
            currentValue += x-1
            sum += currentValue  
    return sum