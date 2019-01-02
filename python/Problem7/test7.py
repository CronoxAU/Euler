import unittest
import problem7

class Test_TestProblem7(unittest.TestCase):

    def test_getNthPrime2(self):
        self.assertEqual(problem7.getNthPrime(2), 3)

    def test_getNthPrime6(self):
        self.assertEqual(problem7.getNthPrime(6), 13)

    def test_getNthPrime100001(self):
        self.assertEqual(problem7.getNthPrime(10001), 104743)

    def test_isPrime1(self):
        self.assertEqual(problem7.isPrime(1), False)

    def test_isPrime2(self):
        self.assertEqual(problem7.isPrime(2), True)

    def test_isPrime5(self):
        self.assertEqual(problem7.isPrime(5), True)
    
    def test_isPrime13(self):
        self.assertEqual(problem7.isPrime(13), True)

    def test_isPrime35(self):
        self.assertEqual(problem7.isPrime(35), False)

    def test_isPrime109(self):
        self.assertEqual(problem7.isPrime(109), True)

    def test_isPrime195(self):
        self.assertEqual(problem7.isPrime(195), False)

    def test_isPrime197(self):
        self.assertEqual(problem7.isPrime(197), True)
    
    def test_isPrime199(self):
        self.assertEqual(problem7.isPrime(199), True)

    def test_isPrime200(self):
        self.assertEqual(problem7.isPrime(200), False)

    def test_isPrime6857(self):
        self.assertEqual(problem7.isPrime(6857), True)

    def test_isPrime6859(self):
        self.assertEqual(problem7.isPrime(6859), False)


if __name__ == '__main__':
    unittest.main()