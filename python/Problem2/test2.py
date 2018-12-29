import unittest
import problem2

class Test_TestProblem1(unittest.TestCase):

    def test_sumEvenFibonacci7(self):
        self.assertEqual(problem2.sumEvenFibonacci(7), 2)

    def test_sumEvenFibonacci9(self):
        self.assertEqual(problem2.sumEvenFibonacci(9), 10)

    def test_sumEvenFibonacci34(self):
        self.assertEqual(problem2.sumEvenFibonacci(34), 10)

    def test_sumEvenFibonacci145(self):
        self.assertEqual(problem2.sumEvenFibonacci(145), 188)

    def test_sumEvenFibonacci1EdgeCaseNegative(self):
        self.assertEqual(problem2.sumEvenFibonacci(-1), 0)

    def test_sumEvenFibonacci1EdgeCase0(self):
        self.assertEqual(problem2.sumEvenFibonacci(0), 0)

    def test_sumEvenFibonacci1EdgeCase1(self):
        self.assertEqual(problem2.sumEvenFibonacci(1), 0)

    def test_sumEvenFibonacci4000000(self):
        self.assertEqual(problem2.sumEvenFibonacci(4000000), 4613732)

if __name__ == '__main__':
    unittest.main()