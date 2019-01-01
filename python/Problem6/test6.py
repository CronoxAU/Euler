import unittest
import problem6

class Test_TestProblem6(unittest.TestCase):

    #sumOfSquares tests
    def test_sumOfSquares1(self):
        self.assertEqual(problem6.sumOfSquares(1), 1)

    def test_sumOfSquares2(self):
        self.assertEqual(problem6.sumOfSquares(2), 5)

    def test_sumOfSquares10(self):
        self.assertEqual(problem6.sumOfSquares(10), 385)

    #squareOfSums Tests
    def test_squareOfSums1(self):
        self.assertEqual(problem6.squareOfSums(1), 1)
    
    def test_squareOfSums1(self):
        self.assertEqual(problem6.squareOfSums(2), 9)

    def test_squareOfSums10(self):
        self.assertEqual(problem6.squareOfSums(10), 3025)

    #sample provided in challenge
    def test_problem6Sample(self):
        self.assertEqual(problem6.diffBetweenSquareOfSumsAndSumOfSquares(10), 2640)

    #Solution needed to complete challenge
    def test_lowestEvenlyDivisibleByAll20(self):
        self.assertEqual(problem6.diffBetweenSquareOfSumsAndSumOfSquares(20), 0)


if __name__ == '__main__':
    unittest.main()