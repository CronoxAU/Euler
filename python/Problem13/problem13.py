#Solution to Project Euler problem 13 - https://projecteuler.net/problem=13
#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers


#returns the sum of the supplied string of numbers, where numbers are differentiated by a newline (\n)
def sumStringOfNumbers(str):
    str = [int(i) for i in str.split("\n")]
    return sum(str)

#returns for first <digits> digits of supplied number <num>
def getFirstDigits(num, digits):
    return int(str(num)[:digits])