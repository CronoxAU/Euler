#Solution to Project Euler problem 14 - https://projecteuler.net/problem=14
#Longest Collatz sequence - Which starting number, under one million, produces the longest chain?


#returns the number of terms in the Collatz sequence starting from n
def numOfTermsInCollatzSeq(n):
  numOfTerms = 1
  while n != 1:
    if(n % 2 == 0):
      n = n/2
    else:
      n = 3*n +1
    numOfTerms += 1
  return numOfTerms


#returns the longest Collatz sequence with a starting number below n
def longestCollatzSeq(n):
  longestSeq = 0
  nWithLongestSeq = 0
  for i in range(1,n+1):
    currentSeq = numOfTermsInCollatzSeq(i)
    if(currentSeq > longestSeq):
      longestSeq = currentSeq
      nWithLongestSeq = i
  return nWithLongestSeq
