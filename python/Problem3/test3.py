import unittest
import problem3

class Test_TestProblem1(unittest.TestCase):

    def test_isPrime1(self):
        self.assertEqual(problem3.isPrime(1), False)

    def test_isPrime2(self):
        self.assertEqual(problem3.isPrime(2), False)

    def test_isPrime5(self):
        self.assertEqual(problem3.isPrime(5), True)
    
    def test_isPrime13(self):
        self.assertEqual(problem3.isPrime(13), True)

    def test_isPrime35(self):
        self.assertEqual(problem3.isPrime(35), False)

    def test_isPrime109(self):
        self.assertEqual(problem3.isPrime(109), True)

    def test_isPrime195(self):
        self.assertEqual(problem3.isPrime(195), False)

    def test_isPrime197(self):
        self.assertEqual(problem3.isPrime(197), True)
    
    def test_isPrime199(self):
        self.assertEqual(problem3.isPrime(199), True)

    def test_isPrime200(self):
        self.assertEqual(problem3.isPrime(200), False)

    def test_isPrime6857(self):
        self.assertEqual(problem3.isPrime(6857), True)

    def test_isPrime6859(self):
        self.assertEqual(problem3.isPrime(6859), False)

    def test_largestPrimeFactor13195(self):
        self.assertEqual(problem3.largestPrimeFactor(13195), 29)

    def test_largestPrimeFactor600851475143(self):
        self.assertEqual(problem3.largestPrimeFactor(600851475143), 6857)

if __name__ == '__main__':
    unittest.main()