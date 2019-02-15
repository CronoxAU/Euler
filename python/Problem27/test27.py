import unittest
import problem27

class Test_TestProblem27(unittest.TestCase):
    def test_isPrime10(self):
        self.assertEqual(problem27.isPrime(10), False)

    def test_maxQuadraticPrimeFormular10(self):
        self.assertEqual(problem27.maxQuadraticPrimeFormular(10), 983)

    #test of full solution
    def test_maxQuadraticPrimeFormular1000(self):
        self.assertEqual(problem27.maxQuadraticPrimeFormular(1000), 983)

if __name__ == '__main__':
    unittest.main()