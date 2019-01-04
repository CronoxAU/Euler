import unittest
import problem7

class Test_TestProblem7(unittest.TestCase):

    def test_getNthPrime2(self):
        self.assertEqual(problem7.getNthPrime(2), 3)

    def test_getNthPrime6(self):
        self.assertEqual(problem7.getNthPrime(6), 13)

    def test_getNthPrime100001(self):
        self.assertEqual(problem7.getNthPrime(10001), 104743)

if __name__ == '__main__':
    unittest.main()