# Solution to Project Euler problem 30 - https://projecteuler.net/problem=30
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# returns true if the number n is a sum of of the mth powers of it's digits
def isSumOfMthPowers(n,m):
    sum = 0
    i = n
    while i > 0:
        currentDigit = i % 10
        sum += currentDigit ** m
        i = i //10
    if sum == n:
        return True
    return False



# returns the sum of all numbers which are the sum of each of their digits raised to the mth power
def sumOfAllMthPower(m):
    sum = 0
    # To find a lose upper limit calculate the 9^m, then multiply that by it's number of digits. 
    # After this upper limit no numbers will sum high enough as even if every digit is 9 the sum will be lower than itself.
    singleDigitLimit = 9 ** m
    limit = (singleDigitLimit * len(str(singleDigitLimit))) + 1

    #as per the definition of the problem start at 2 because 1 is excluded.
    for i in range(2, limit):
        if isSumOfMthPowers(i,m):
            sum += i
    return sum