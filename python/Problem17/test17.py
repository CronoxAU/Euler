import unittest
import problem17

class Test_TestProblem17(unittest.TestCase):

    def test_toWritten1(self):
        self.assertEqual(problem17.toWritten(1), "one")

    def test_toWritten27(self):
        self.assertEqual(problem17.toWritten(27), "twenty seven")

    def test_toWritten100(self):
        self.assertEqual(problem17.toWritten(100), "one hundred")

    def test_toWritten101(self):
        self.assertEqual(problem17.toWritten(101), "one hundred and one")

    def test_toWritten965(self):
        self.assertEqual(problem17.toWritten(965), "nine hundred and sixty five")

    def test_toWritten800(self):
        self.assertEqual(problem17.toWritten(800), "eight hundred")

    def test_toWritten1000(self):
        self.assertEqual(problem17.toWritten(1000), "one thousand")

    def test_toWritten56814(self):
        self.assertEqual(problem17.toWritten(56814), "fifty six thousand eight hundred and fourteen")

    def test_toWritten75423(self):
        self.assertEqual(problem17.toWritten(75423), "seventy five thousand four hundred and twenty three")

    
    def test_removeSpacesAndHyphens75423(self):
        self.assertEqual(problem17.removeSpacesAndHyphens("seventy five thousand four hundred and twenty three"), "seventyfivethousandfourhundredandtwentythree")

    def test_numberLetterCount75423(self):
        self.assertEqual(problem17.numberLetterCount(75423,75423), len("seventyfivethousandfourhundredandtwentythree"))

    def test_numberLetterCount1to5(self):
        self.assertEqual(problem17.numberLetterCount(1,5), 19)

    #test of full solution
    def test_numberLetterCount1to1000(self):
        self.assertEqual(problem17.numberLetterCount(1,1000), 21124)

if __name__ == '__main__':
    unittest.main()