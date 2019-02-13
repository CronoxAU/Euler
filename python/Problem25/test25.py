import unittest
import problem25

class Test_TestProblem25(unittest.TestCase):
    def test_indexOfFirstFibonacciWithNDigits1(self):
        self.assertEqual(problem25.indexOfFirstFibonacciWithNDigits(1), 1)

    def test_indexOfFirstFibonacciWithNDigits2(self):
        self.assertEqual(problem25.indexOfFirstFibonacciWithNDigits(2), 7)
    
    def test_indexOfFirstFibonacciWithNDigits3(self):
        self.assertEqual(problem25.indexOfFirstFibonacciWithNDigits(3), 12)
        

    #test of full solution
    def test_indexOfFirstFibonacciWithNDigits1000(self):
        self.assertEqual(problem25.indexOfFirstFibonacciWithNDigits(1000), 4782)

if __name__ == '__main__':
    unittest.main()