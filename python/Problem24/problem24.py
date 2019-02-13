# Solution to Project Euler problem 24 - https://projecteuler.net/problem=24
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools

# This one is a bit of a cheat using the tools in python
# Fortunatly this results in a solution which is still very quick
# If this has been slower I would have looked at an option for caclulating the nth permutation without actually generating any of the other permutations using factorials
# or at least filtered the search sapce based on this infromation, for example 9! is 362,880, 
# the 1,000,00th item must be in the 3 group of 362880 permutations (between 725,760 and 1,088,640) so from that we know the first digit must be 2
# 8! is 40,320, adding this to the 725,760 starting point we can see the second digit must be 7, leaving us in the range 967,680 to 1,008,000

# Generate lexicographic permutations from supplied list
# returns an ordered list of permutations
def generateLexicographicPermutation(digits):
    return list(itertools.permutations(digits))

def nthPermutation(n ,digits):
    return generateLexicographicPermutation(digits)[n-1]

