import unittest
import problem23

class Test_TestProblem21(unittest.TestCase):

    def test_sumOfFactors2(self):
        self.assertEqual(problem23.sumOfFactors(2), 1)

    def test_sumOfFactors4(self):
        self.assertEqual(problem23.sumOfFactors(4), 3)

    def test_sumOfFactors12(self):
        self.assertEqual(problem23.sumOfFactors(12), 16)

    def test_isAbundant4(self):
        self.assertEqual(problem23.isAbundant(4), False)

    def test_isAbundant12(self):
        self.assertEqual(problem23.isAbundant(12), True)

    def test_isSumFromList1(self):
        self.assertEqual(problem23.isSumFromList(1,[0,4,5,6]), False)

    def test_isSumFromList9(self):
        self.assertEqual(problem23.isSumFromList(9,[0,4,5,6]), True)  

    def test_generateAbundantList11(self):
        self.assertEqual(problem23.generateAbundantList(11), [])

    def test_generateAbundantList12(self):
        self.assertEqual(problem23.generateAbundantList(12), [12])
        
    #test of full solution
    def test_fullSolution(self):
        self.assertEqual(problem23.fullSolution(28123), 0)

if __name__ == '__main__':
    unittest.main()