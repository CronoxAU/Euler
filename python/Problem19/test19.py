import unittest
import problem19

class Test_TestProblem19(unittest.TestCase):

    def test_day_of_week20thJan2019(self):
        self.assertEqual(problem19.day_of_week(2019,1,20), 6)

    #test of full solution
    def test_sundaysOnFirstDayFullSolution(self):
       self.assertEqual(problem19.sundaysOnFirstDay(1901,2000), 171)

if __name__ == '__main__':
    unittest.main()