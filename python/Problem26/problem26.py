# Solution to Project Euler problem 26 - https://projecteuler.net/problem=26
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


def recurringLength(n):
    p = 1
    while (10 ** p) % n != 1:
        p +=1
    return p

def maxRecurringLength(limit):
    maxNumber = 0
    maxValue = 0
    for i in range(1,limit):
        currentValue = recurringDecimalLength(1,i)
        if(currentValue > maxValue):
            maxNumber = i
    return maxNumber