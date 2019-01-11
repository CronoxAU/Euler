import unittest
import problem12

class Test_TestProblem12(unittest.TestCase):


    def test_getNumberOfDivisors1(self):
        self.assertEqual(problem12.getNumberOfDivisors(1), 1)

    def test_getNumberOfDivisors3(self):
        self.assertEqual(problem12.getNumberOfDivisors(3), 2)

    def test_getNumberOfDivisors6(self):
        self.assertEqual(problem12.getNumberOfDivisors(6), 4)

    def test_getNumberOfDivisors12(self):
        self.assertEqual(problem12.getNumberOfDivisors(12), 6)

    def test_getNumberOfDivisors25(self):
        self.assertEqual(problem12.getNumberOfDivisors(25), 3)

    def test_getNumberOfDivisors28(self):
        self.assertEqual(problem12.getNumberOfDivisors(28), 6)

    def test_getLowestTriangleNumberByNoOfDivisors2(self):
        self.assertEqual(problem12.getLowestTriangleNumberByNoOfDivisors(2), 3)

    def test_getLowestTriangleNumberByNoOfDivisors4(self):
        self.assertEqual(problem12.getLowestTriangleNumberByNoOfDivisors(4), 6)

    def test_getLowestTriangleNumberByNoOfDivisors28(self):
        self.assertEqual(problem12.getLowestTriangleNumberByNoOfDivisors(6), 28)

    def test_getLowestTriangleNumberByNoOfDivisors500(self):
        self.assertEqual(problem12.getLowestTriangleNumberByNoOfDivisors(500), 76576500)

if __name__ == '__main__':
    unittest.main()