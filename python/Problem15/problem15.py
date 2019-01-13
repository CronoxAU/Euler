#Solution to Project Euler problem 15 - https://projecteuler.net/problem=15
#How many such routes are there through a 20×20 grid?

#Notes:
# - Number of steps in a path will always be the same for a give grid with the number of steps being the sum of the dimensions, is this useful?
# - Each move in a given path can be represented as a choice from an alphabet of two different options, lets use D as down and R as right
# for a 1x1 grid this would be DR and RD, for a 2x2 the solutions are DDRR, DRDR, RRDD, RDRD, DRRD, RDDR
# can we find an equation/algorithm to find all unique combinations of a given length string for a 2 letter alphabet?
# the unusual restriction here is that while characters can appear in any order, each of the two characters must appear the same number of times

# - Solve of recursively going through each potential step, taking both the right and down path?
# - Working manually the paths to solve square grids, starting at 1x1 are - 2, 6, 20

def countPathsRecursively(x,y,limit):
  # if both x and y are under the limit, explore down both paths
  # if there is at the limit, there is only 1 valid path left (either all right or all down) so return 1
  if x < limit and y < limit:
    return countPathsRecursively(x+1, y, limit) + countPathsRecursively(x, y+1, limit)
  else:
    return 1


#returns the number of possible lattice paths through a square grid of the given dimensions n
def latticePathsInSquareGrid(n):
  countOfPaths = 0

  return countOfPaths
