import math 

def isPrime(num):
  if num <= 1: return False
  if num == 2: return True
  if num % 2 == 0: return False
  upperLimit = math.floor(math.sqrt(num))
  #we can increment i by 2 as every skipped value will be even and thus the %2 factor check above would have matched
  for i in range(3,upperLimit+1, 2):
      if num % i == 0:
        return False
  return True
