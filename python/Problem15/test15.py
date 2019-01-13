import unittest
import problem15

class Test_TestProblem15(unittest.TestCase):

    def test_countPathsRecursively1(self):
        self.assertEqual(problem15.countPathsRecursively(0,0,1), 2)
    
    def test_countPathsRecursively2(self):
        self.assertEqual(problem15.countPathsRecursively(0,0,2), 6)

    def test_countPathsRecursively3(self):
        self.assertEqual(problem15.countPathsRecursively(0,0,3), 20)

    #test of full solution
    def test_countPathsRecursively20(self):
        self.assertEqual(problem15.countPathsRecursively(0,0,20), 137846528820)

if __name__ == '__main__':
    unittest.main()