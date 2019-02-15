# Solution to Project Euler problem 26 - https://projecteuler.net/problem=26
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# Notes:
# See https://en.wikipedia.org/wiki/Repeating_decimal for samples and details


def recurringLengthOfUnitFraction(n):
    remainderLog = []
    remainder = 1
    while True:
        #raise the existing remainder by 10, as we are moving left one digit then calculate the new remainder
        remainder = (remainder*10)%n
        # if the remainder is 0 we have reached an even division, and there is no recurring section
        if remainder == 0:
            return 0
        # if the current remainder already exists in our log we are ad the start of a new sequence, return the number of elements in the log since
        # this number last appeared as the length of the recurring portion
        if remainder in remainderLog:
            return len(remainderLog) - remainderLog.index(remainder)
        remainderLog.append(remainder)

def maxUnitFractionRecurringLength(limit):
    maxI = 0
    maxLength = 0
    for i in range(1,limit):
        currentLength = recurringLengthOfUnitFraction(i)
        if(currentLength > maxLength):
            maxI = i
            maxLength = currentLength
    return maxI