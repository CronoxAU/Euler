import unittest
import problem23

class Test_TestProblem23(unittest.TestCase):

    # sumOfFactors function
    def test_sumOfFactors1(self):
        self.assertEqual(problem23.sumOfFactors(1), 1)

    def test_sumOfFactors2(self):
        self.assertEqual(problem23.sumOfFactors(2), 1)

    def test_sumOfFactors4(self):
        self.assertEqual(problem23.sumOfFactors(4), 3)

    def test_sumOfFactors12(self):
        self.assertEqual(problem23.sumOfFactors(12), 16)

    def test_sumOfFactors25(self):
        self.assertEqual(problem23.sumOfFactors(25), 6)


    # isAbundant function
    def test_isAbundant4(self):
        self.assertEqual(problem23.isAbundant(4), False)

    def test_isAbundant12(self):
        self.assertEqual(problem23.isAbundant(12), True)

    def test_isAbundant1(self):
        self.assertEqual(problem23.isSumFromList(1,[0,4,5,6]), False)

    # canBeWrittenAsSum Function
    def test_canBeWrittenAsSum3(self):
        self.assertEqual(problem23.canBeWrittenAsSum([1,1,2,3,11,15],3), [0,0,1,1])

    def test_canBeWrittenAsSum10(self):
        self.assertEqual(problem23.canBeWrittenAsSum([1,1,2,3,11,15],10), [0,0,1,1,1,1,1,0,0,0,0])


    # isSumFromList function
    def test_isSumFromList3(self):
        self.assertEqual(problem23.isSumFromList(3,[0,4,5,6]), False)  

    def test_isSumFromList9(self):
        self.assertEqual(problem23.isSumFromList(9,[0,4,5,6]), True)  

    # generateAbundantList function
    def test_generateAbundantList11(self):
        self.assertEqual(problem23.generateAbundantList(11), [])

    def test_generateAbundantList12(self):
        self.assertEqual(problem23.generateAbundantList(12), [12])

    # generateListOfSums function
    def test_generateListOfSums(self):
        self.assertEqual(problem23.generateListOfSums([1,2,3],7), [2,3,4,5,6])

    def test_generateListOfSumsLimit(self):
        self.assertEqual(problem23.generateListOfSums([1,2,3],3), [2,3])


    # sumList function
    def test_sumList(self):
        self.assertEqual(problem23.sumList([1,2,3]), 6)
        
    # triangleNumber function
    def test_triangleNumber1(self):
        self.assertEqual(problem23.triangleNumber(1), 1)

    def test_triangleNumber3(self):
        self.assertEqual(problem23.triangleNumber(3), 6)


    # deduplicateList function
    def test_deduplicateList1(self):
        self.assertEqual(problem23.deduplicateList([1,1,1,1,1,2]), [1,2])

    def test_deduplicateList2(self):
        self.assertEqual(problem23.deduplicateList([1,2]), [1,2])

    # sumOfNonAbundantSums function 
    def test_sumOfNonAbundantSums11(self):
        self.assertEqual(problem23.sumOfNonAbundantSums(11), 66)

    def test_sumOfNonAbundantSums200(self):
        self.assertEqual(problem23.sumOfNonAbundantSums(200), 10266)

    def test_sumOfNonAbundantSums2000(self):
        self.assertEqual(problem23.sumOfNonAbundantSums(2000), 573153)

    def test_sumOfNonAbundantSums10000(self):
        self.assertEqual(problem23.sumOfNonAbundantSums(10000), 3731004)

    #test of full solution
    def test_sumOfNonAbundantSums28123(self):
        self.assertEqual(problem23.sumOfNonAbundantSums(28123), 4179871)

if __name__ == '__main__':
    unittest.main()