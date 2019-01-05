import unittest
import problem8

class Test_TestProblem8(unittest.TestCase):

    def test_getHighestProduct4(self):
        self.assertEqual(problem8.getHighestProduct(4), 5832)

    def test_getHighestProduct5(self):
        self.assertEqual(problem8.getHighestProduct(5), 40824)

    def test_getHighestProduct13(self):
        self.assertEqual(problem8.getHighestProduct(13), 23514624000)

    def test_getProduct1234(self):
        self.assertEqual(problem8.getProduct('1234'), 24)

    def test_getProduct55555(self):
        self.assertEqual(problem8.getProduct('55555'), 3125)
    
    def test_getProduct9989(self):
        self.assertEqual(problem8.getProduct('9989'), 5832)
        

if __name__ == '__main__':
    unittest.main()