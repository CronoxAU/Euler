import unittest
import problem17

class Test_TestProblem17(unittest.TestCase):

    def test_toWritten1(self):
        self.assertEqual(problem17.toWritten(1), "one")

    def test_numberLetterCount1to5(self):
        self.assertEqual(problem17.numberLetterCount(1,5), 19)

    #test of full solution
    def test_numberLetterCount1to1000(self):
        self.assertEqual(problem17.numberLetterCount(1,1000), 19)

if __name__ == '__main__':
    unittest.main()