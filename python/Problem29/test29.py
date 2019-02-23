import unittest
import problem29

class Test_TestProblem29(unittest.TestCase):
    def test_distinctPowersa2b2(self):
        self.assertEqual(problem29.distinctPowers(2,2), 1)

    def test_distinctPowersa5b5(self):
        self.assertEqual(problem29.distinctPowers(5,5), 15)

    #test of full solution
    def test_distinctPowersa100b100(self):
        self.assertEqual(problem29.distinctPowers(100,100), 9183)

if __name__ == '__main__':
    unittest.main()