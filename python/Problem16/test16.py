import unittest
import problem16

class Test_TestProblem16(unittest.TestCase):

    def test_sumDigits5(self):
        self.assertEqual(problem16.sumDigits(5), 5)

    def test_sumDigits10(self):
        self.assertEqual(problem16.sumDigits(10), 1)

    def test_sumDigitsSample(self):
        self.assertEqual(problem16.sumDigits(2**15), 26)

    #test of full solution
    def test_sumDigitsFinalSolution(self):
        self.assertEqual(problem16.sumDigits(2**1000), 1366)

if __name__ == '__main__':
    unittest.main()