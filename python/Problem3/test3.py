import unittest
import problem3

class Test_TestProblem3(unittest.TestCase):

    def test_largestPrimeFactor13195(self):
        self.assertEqual(problem3.largestPrimeFactor(13195), 29)

    def test_largestPrimeFactor600851475143(self):
        self.assertEqual(problem3.largestPrimeFactor(600851475143), 6857)

if __name__ == '__main__':
    unittest.main()