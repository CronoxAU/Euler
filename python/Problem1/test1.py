import unittest
import problem1

class Test_TestProblem1(unittest.TestCase):

    def test_sumMultiplesBase1Upper1(self):
        self.assertEqual(problem1.sumMultiples(1,1), 0)

    def test_sumOfMultiplesHandlesBase1Upper2(self):
        self.assertEqual(problem1.sumMultiples(1,2), 1)

    def test_sumOfMultiplesHandlesBase0(self):
        self.assertEqual(problem1.sumMultiples(0,100), 0)
    
    def test_sumOfMultiplesHandlesBaseNegative(self):
        self.assertEqual(problem1.sumMultiples(-50,100), 0)
    
    def test_sumOfMultiplesHandlesInitialSample(self):
        self.assertEqual(problem1.sumMultiples(5,10), 5)
    
    def test_uniqueSumOfTwoMultiplesHandlesInitialSample(self):
        self.assertEqual(problem1.uniqueSumOfTwoMultiples(3,5,10), 23)
    
    def test_uniqueSumOfTwoMultiplesHandlesFinalAnswer(self):
        self.assertEqual(problem1.uniqueSumOfTwoMultiples(3,5,1000), 233168)

if __name__ == '__main__':
    unittest.main()