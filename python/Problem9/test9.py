import unittest
import problem9

class Test_TestProblem9(unittest.TestCase):

    def test_isPythagoreanTriplet345(self):
        self.assertEqual(problem9.isPythagoreanTriplet(3,4,5), True)

    def test_isPythagoreanTriplet354(self):
        self.assertEqual(problem9.isPythagoreanTriplet(3,5,4), False)
        
    def test_getProductOfPythagoreanTripletBySum25(self):
        self.assertEqual(problem9.getProductOfPythagoreanTripletBySum(12), 60)

    def test_getProductOfPythagoreanTripletBySum1000(self):
        self.assertEqual(problem9.getProductOfPythagoreanTripletBySum(1000), 31875000)   

if __name__ == '__main__':
    unittest.main()