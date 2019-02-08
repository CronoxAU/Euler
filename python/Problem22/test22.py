import unittest
import problem22

class Test_TestProblem22(unittest.TestCase):

    def test_letterScorea(self):
        self.assertEqual(problem22.letterScore('a'), 1)

    def test_letterScoreC(self):
        self.assertEqual(problem22.letterScore('C'), 3)

    def test_letterScorez(self):
        self.assertEqual(problem22.letterScore('z'), 26)
    
    def test_letterScore1(self):
        self.assertEqual(problem22.letterScore('1'), 0)

    def test_letterScoreSpace(self):
        self.assertEqual(problem22.letterScore(' '), 0)

    def test_stringScoreAB(self):
        self.assertEqual(problem22.stringScore('AB'), 3) 

    def test_stringScoreCOLIN(self):
        self.assertEqual(problem22.stringScore('COLIN'), 53) 

    def test_caclulateNameScoreTest1(self):
        self.assertEqual(problem22.caclulateNameScore("test1.txt"), 5)

    def test_caclulateNameScoreTest2(self):
        self.assertEqual(problem22.caclulateNameScore("test2.txt"), 14)    

    def test_caclulateNameScoreTest3(self):
        self.assertEqual(problem22.caclulateNameScore("test3.txt"), 0)     
        
    #test of full solution
    def test_caclulateNameScoreFullTest(self):
        self.assertEqual(problem22.caclulateNameScore("p022_names.txt"), 0)

if __name__ == '__main__':
    unittest.main()