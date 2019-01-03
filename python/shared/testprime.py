import unittest
import prime

class Test_TestPrimeFunctions(unittest.TestCase):

    def test_isPrime1(self):
        self.assertEqual(prime.isPrime(1), False)

    def test_isPrime2(self):
        self.assertEqual(prime.isPrime(2), True)

    def test_isPrime5(self):
        self.assertEqual(prime.isPrime(5), True)
    
    def test_isPrime13(self):
        self.assertEqual(prime.isPrime(13), True)

    def test_isPrime35(self):
        self.assertEqual(prime.isPrime(35), False)

    def test_isPrime109(self):
        self.assertEqual(prime.isPrime(109), True)

    def test_isPrime195(self):
        self.assertEqual(prime.isPrime(195), False)

    def test_isPrime197(self):
        self.assertEqual(prime.isPrime(197), True)
    
    def test_isPrime199(self):
        self.assertEqual(prime.isPrime(199), True)

    def test_isPrime200(self):
        self.assertEqual(prime.isPrime(200), False)

    def test_isPrime6857(self):
        self.assertEqual(prime.isPrime(6857), True)

    def test_isPrime6859(self):
        self.assertEqual(prime.isPrime(6859), False)


if __name__ == '__main__':
    unittest.main()