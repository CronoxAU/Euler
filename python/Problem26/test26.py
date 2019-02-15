import unittest
import problem26

class Test_TestProblem26(unittest.TestCase):
    def test_recurringLengthOfUnitFraction3(self):
        self.assertEqual(problem26.recurringLengthOfUnitFraction(3), 1)

    def test_recurringLengthOfUnitFraction7(self):
        self.assertEqual(problem26.recurringLengthOfUnitFraction(7), 6)

    def test_recurringLengthOfUnitFraction9(self):
        self.assertEqual(problem26.recurringLengthOfUnitFraction(9), 1)

    def test_recurringLengthOfUnitFraction28(self):
        self.assertEqual(problem26.recurringLengthOfUnitFraction(28), 6)

    def test_recurringLengthOfUnitFraction43(self):
        self.assertEqual(problem26.recurringLengthOfUnitFraction(43), 21)
        
    
    def test_maxUnitFractionRecurringLength10(self):
        self.assertEqual(problem26.maxUnitFractionRecurringLength(10), 7)

    #test of full solution
    def test_maxUnitFractionRecurringLength1000(self):
        self.assertEqual(problem26.maxUnitFractionRecurringLength(1000), 983)

if __name__ == '__main__':
    unittest.main()