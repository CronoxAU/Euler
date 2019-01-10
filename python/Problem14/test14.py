import unittest
import problem14

class Test_TestProblem14(unittest.TestCase):

    def test_numOfTermsInCollatzSeq1(self):
        self.assertEqual(problem14.numOfTermsInCollatzSeq(1), 1)

    def test_numOfTermsInCollatzSeq13(self):
        self.assertEqual(problem14.numOfTermsInCollatzSeq(13), 10)
        
    def test_numOfTermsInCollatzSeq259(self):
        self.assertEqual(problem14.numOfTermsInCollatzSeq(259), 123)

    def test_numOfTermsInCollatzSeq837799(self):
        self.assertEqual(problem14.numOfTermsInCollatzSeq(837799), 525)
    
    def test_longestCollatzSeq2(self):
        self.assertEqual(problem14.longestCollatzSeq(2), 2)

    #test of full solution
    def test_longestCollatzSeq999999(self):
        self.assertEqual(problem14.longestCollatzSeq(999999), 837799)

if __name__ == '__main__':
    unittest.main()