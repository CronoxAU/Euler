#Solution to Project Euler problem 2 - https://projecteuler.net/problem=2
#Find the sum of all even Fibonacci numbers below 4,000,000


def sumEvenFibonacci(upperLimit):
  current = 0
  previous1 = 0
  previous2 = 1
  sum = 0

  while current < upperLimit:
    if (current % 2) == 0:
      sum = sum + current
    current = previous1 + previous2
    previous2 = previous1
    previous1 = current
  return sum

result = sumEvenFibonacci(4000000)
print(result)