import unittest
import problem24

class Test_TestProblem24(unittest.TestCase):
    def test_generateLexicographicPermutation123(self):
        self.assertEqual(problem24.generateLexicographicPermutation([0,1,2]), [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)])

    def test_nthPermutation123(self):
        self.assertEqual(problem24.nthPermutation(3, [0,1,2]), (1,0,2))
        

    #test of full solution
    def test_FullSolution(self):
        self.assertEqual(problem24.nthPermutation(1000000, [0,1,2,3,4,5,6,7,8,9]), (2, 7, 8, 3, 9, 1, 5, 4, 6, 0))

if __name__ == '__main__':
    unittest.main()