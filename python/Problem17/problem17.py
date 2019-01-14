#Solution to Project Euler problem 17 - https://projecteuler.net/problem=17
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 

#returns the written form on the supplied number n
def toWritten(n):
  #notes
  #numbers can be broken into groups of three digits, which can be processed together then have the correct siffix term added (thousand, million, billion etc.)
  #In these groups of three the most significant digit is ignored if it is 0 and the standard term for the number is always used otherwise (one, two, three etc.) with hundred added as a suffix term
  #If the most significant digit is not 0, and there is a digit in the second or third position the term "and" should be added (eg seven hundred and twenty two)
  #For the second digit if it is 0 it is again ignored, if it is 1 the result depends on the third digit, while all other numbers have their own unique "10's" form (twenty, thirty etc.)
  #For the third digit, if the second digit is 1 each third digit has it's own unique "teen" form (ten, eleven, twelve, thirteen etc.), otherwise the ruls of the most significant ....
  # digit apply with 0 being ignored and the other numbers using there standard term (one, two, three etc.)
  writtenNumber = ""
  standardWritten = ["","one", "two", "three", "four","five","six","seven","eight","nine"]
  tensWritten = ["","", "twenty", "thirty", "fourty","fifty","sixty","seventy","eighty","ninty"]
  teensWritten = ["ten","eleven", "twelve", "thirteen", "fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
  #Work through number in groups of 3 digits
  while n > 0:
    currentWritten 
    currentN += n%1000
    n //= 1000
  return writtenNumber

#returns the sum of all letters in the written version of numbers between x and y, inclusive.
def numberLetterCount(x, y):
  count = 0
  for i in range(x,y+1):
    count = len()
  return count
