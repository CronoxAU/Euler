import unittest
import problem27

class Test_TestProblem27(unittest.TestCase):

    def test_maxQuadraticPrimeFormular10(self):
        self.assertEqual(problem27.maxQuadraticPrimeFormular(10), (-3, 7, 6))

    
    def test_maxQuadraticPrimeFormular1000(self):
        self.assertEqual(problem27.maxQuadraticPrimeFormular(1000), (-61, 971, 71))

    #test of full solution
    def test_maxQuadraticPrimeProduct1000(self):
        self.assertEqual(problem27.maxQuadraticPrimeProduct(1000), -59231)

if __name__ == '__main__':
    unittest.main()