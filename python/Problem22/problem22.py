#Solution to Project Euler problem 22 - https://projecteuler.net/problem=22
#What is the total of all the name scores in the file?

#returns the score of the letter l based on it's position in the alphabet (A=1, B=2, C=3 etc.)
#ensure the letter is lowercase, then convert it to ASCII and subrtact 96 from the result
def letterScore(l):
  result = 0
  if l.isalpha():
    result =  ord(l.lower()) - 96
  return result

#calculates the combines score of the letters in the supplied string s, based on their position in the aphhabet
# for example COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53
def stringScore(s):
  score = 0
  for c in s:
    score += letterScore(c)
  return score

def calculateNameScore(file):
  #load the file into an array
  for data in open(file):
    data = data.replace('"','')
    names = data.split(",")
  #sort the array
  names = sorted(names, key=str.lower)
  #score the array
  score = 0
  for i in range(0,len(names)):
    score += (i+1) * stringScore(names[i])
  return score