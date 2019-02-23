import unittest
import problem28

class Test_TestProblem28(unittest.TestCase):
    def test_sumOfSpiralDiagonals1(self):
        self.assertEqual(problem28.sumOfSpiralDiagonals(1), 1)

    def test_sumOfSpiralDiagonals3(self):
        self.assertEqual(problem28.sumOfSpiralDiagonals(3), 25)

    def test_sumOfSpiralDiagonals5(self):
        self.assertEqual(problem28.sumOfSpiralDiagonals(5), 101)

    #test of full solution
    def test_sumOfSpiralDiagonals1001(self):
        self.assertEqual(problem28.sumOfSpiralDiagonals(1001), 669171001)

if __name__ == '__main__':
    unittest.main()