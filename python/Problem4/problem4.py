#Solution to Project Euler problem 4 - https://projecteuler.net/problem=4
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(num):
  original = str(num)
  reverse = original[::-1]
  if(original == reverse):
    return True
  return False

result = 1
print(result)