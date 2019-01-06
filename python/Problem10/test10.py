import unittest
import problem10

class Test_TestProblem10(unittest.TestCase):

    def test_getSumOfPrimes10(self):
        self.assertEqual(problem10.getSumOfPrimes(10), 17)

    def test_getSumOfPrimes2000000(self):
        self.assertEqual(problem10.getSumOfPrimes(2000000), 142913828922)

if __name__ == '__main__':
    unittest.main()