import unittest
import problem21

class Test_TestProblem21(unittest.TestCase):

    def test_sumOfFactors2(self):
        self.assertEqual(problem21.sumOfFactors(2), 1)

    def test_sumOfFactors24(self):
        self.assertEqual(problem21.sumOfFactors(4), 3)

    def test_sumOfFactors220(self):
        self.assertEqual(problem21.getAmicablePair(220), 284)

    def test_getAmicablePair785(self):
        self.assertEqual(problem21.getAmicablePair(785), 0)

    def test_getAmicablePair220(self):
        self.assertEqual(problem21.getAmicablePair(220), 284)

    def test_getAmicablePair284(self):
        self.assertEqual(problem21.getAmicablePair(284), 220)

    def test_sumAmicableNumbers500(self):
        self.assertEqual(problem21.sumAmicableNumbers(500), 504)
        
    #test of full solution
    def test_sumAmicableNumbers10000(self):
        self.assertEqual(problem21.sumAmicableNumbers(10000), 0)

if __name__ == '__main__':
    unittest.main()