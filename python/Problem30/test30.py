import unittest
import problem30

class Test_TestProblem29(unittest.TestCase):
    def test_isSumOfMthPowersN1634M4(self):
        self.assertEqual(problem30.isSumOfMthPowers(1634,4), True)

    def test_isSumOfMthPowersN1634M5(self):
        self.assertEqual(problem30.isSumOfMthPowers(1634,5), False)

    def test_sumOfAllMthPower(self):
        self.assertEqual(problem30.sumOfAllMthPower(4), 19316)

    #test of full solution
    #def test_sumOfAllMthPower(self):
    #    self.assertEqual(problem30.distinctPowers(5), 0)

if __name__ == '__main__':
    unittest.main()