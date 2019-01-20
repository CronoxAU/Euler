#Solution to Project Euler problem 18 - https://projecteuler.net/problem=18
#Maximum path sum

#Work from the bottom to the top
#work through each position taking the highest number from the two below positions and adding that to the current position to produce the maximum sum for that position.
#Once we work through the whole triangle the number in the top position should be the highest possible sum

def maxSumTriangle(triData):
  #loop through the rows starting at the second bottom row
  for row in range(len(triData)-2, -1, -1):
    for position in range(0, len(triData[row])):
      triData[row][position] = max(triData[row+1][position], triData[row+1][position+1]) + triData[row][position]
  return triData[0][0]
