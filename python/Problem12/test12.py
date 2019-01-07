import unittest
import problem12

class Test_TestProblem12(unittest.TestCase):

    def test_getNumberOfDivisors3(self):
        arr = [[10,9],[2,5]]
        self.assertEqual(problem11.getNumberOfDivisors(3), 2)

if __name__ == '__main__':
    unittest.main()