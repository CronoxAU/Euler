import unittest
import problem31

class Test_TestProblem31(unittest.TestCase):

    def test_getTotalFromCoins1p(self):
        self.assertEqual(problem31.getTotalFromCoins(0,0,0,0,0,0,0,1), 1)

    def test_getTotalFromCoins2P(self):
        self.assertEqual(problem31.getTotalFromCoins(2,0,0,0,0,0,0,0), 400)

    def test_getTotalFromCoinsOneOfEach(self):
        self.assertEqual(problem31.getTotalFromCoins(1,1,1,1,1,1,1,1), 388)

    def test_numberOfWaysToMakeNPounds1p(self):
        self.assertEqual(problem31.numberOfWaysToMakeNPounds(.01), 1)

    def test_numberOfWaysToMakeNPoundsV21p(self):
        self.assertEqual(problem31.numberOfWaysToMakeNPoundsV2(.01), 1)
    
    def test_numberOfWaysToMakeNPounds2p(self):
        self.assertEqual(problem31.numberOfWaysToMakeNPounds(.02), 2)

    def test_numberOfWaysToMakeNPoundsV22p(self):
        self.assertEqual(problem31.numberOfWaysToMakeNPoundsV2(.02), 2)

    def test_numberOfWaysToMakeNPounds5p(self):
        self.assertEqual(problem31.numberOfWaysToMakeNPounds(.05), 4)

    def test_numberOfWaysToMakeNPoundsV25p(self):
        self.assertEqual(problem31.numberOfWaysToMakeNPoundsV2(.05), 4)

    def test_numberOfWaysToMakeNPounds6p(self):
        self.assertEqual(problem31.numberOfWaysToMakeNPounds(.06), 5)

    def test_numberOfWaysToMakeNPoundsV26p(self):
        self.assertEqual(problem31.numberOfWaysToMakeNPoundsV2(.06), 5)

    #test of full solution
    def test_numberOfWaysToMakeNPounds2P(self):
        self.assertEqual(problem31.numberOfWaysToMakeNPounds(2), 73682)

    def test_numberOfWaysToMakeNPoundsV22P(self):
        self.assertEqual(problem31.numberOfWaysToMakeNPoundsV2(2), 73682)

if __name__ == '__main__':
    unittest.main()