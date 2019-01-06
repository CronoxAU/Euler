#Solution to Project Euler problem 11 - https://projecteuler.net/problem=11
#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
#97, 87, 94, 89 (15,3)
import math 

#returns largest product of n adjcent numbers in supplied grid
def getLargestProduct(n, grid):
  largestProduct = 0
  height = len(grid)
  width = len(grid[0])
  for i in range(0,height):
    for j in range(0,width):
      #check diagonal down if applicable
      if j <= width - n and i <= height - n:
        tempProduct = grid[i][j]
        for inc in range(1, n):
          tempProduct *= grid[i+inc][j+inc]
        if tempProduct > largestProduct:
          largestProduct = tempProduct
      #check diagonal up if applicable
      if j <= width - n and i >= n-1:
        tempProduct = grid[i][j]
        for inc in range(1, n):
          tempProduct *= grid[i-inc][j+inc]
        if tempProduct > largestProduct:
          largestProduct = tempProduct
      #check vertical if applicable
      if i <= height - n:
        tempProduct = grid[i][j]
        for inc in range(1, n):
          tempProduct *= grid[i+inc][j]
        if tempProduct > largestProduct:
          largestProduct = tempProduct
      #check horizontal if applicable
      if j <= width - n:
        tempProduct = grid[i][j]
        for inc in range(1, n):
          tempProduct *= grid[i][j+inc]
        if tempProduct > largestProduct:
          largestProduct = tempProduct
  return largestProduct

