import unittest
import problem26

class Test_TestProblem26(unittest.TestCase):
    def test_recurringLength3(self):
        self.assertEqual(problem26.recurringLength(3), 1)


    def test_recurringLength28(self):
        self.assertEqual(problem26.recurringLength(28), 6)

    def test_recurringLength43(self):
        self.assertEqual(problem26.recurringLength(43), 21)
        
    
    def test_maxRecurringLength10(self):
        self.assertEqual(problem26.maxRecurringLength(10), 6)

    #test of full solution
    def test_maxRecurringLength100(self):
        self.assertEqual(problem26.maxRecurringLength(100), 0)

if __name__ == '__main__':
    unittest.main()