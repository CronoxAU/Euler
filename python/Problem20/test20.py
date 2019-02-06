import unittest
import problem20
import math

class Test_TestProblem20(unittest.TestCase):

    def test_sumOfDigits4(self):
        self.assertEqual(problem20.sumOfDigits(4), 4)

    def test_sumOfDigits12(self):
        self.assertEqual(problem20.sumOfDigits(12), 3)

    def test_sumOfDigits100(self):
        self.assertEqual(problem20.sumOfDigits(100), 1)

    def test_sumOfDigits10Factorial(self):
        self.assertEqual(problem20.sumOfDigits(math.factorial(10)), 27)

    #test of full solution
    def test_sumOfDigits100Factorial(self):
        self.assertEqual(problem20.sumOfDigits(math.factorial(100)), 648)

if __name__ == '__main__':
    unittest.main()