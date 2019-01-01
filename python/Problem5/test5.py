import unittest
import problem5

class Test_TestProblem5(unittest.TestCase):

    def test_isEvenlyDivisibleByAll2520Limit10(self):
        self.assertEqual(problem5.isEvenlyDivisibleByAll(2520, 10), True)
    
    def test_isEvenlyDivisibleByAll2521Limit10(self):
        self.assertEqual(problem5.isEvenlyDivisibleByAll(2521, 10), False)
    
    def test_isEvenlyDivisibleByAll2520Limit11(self):
        self.assertEqual(problem5.isEvenlyDivisibleByAll(2520, 11), False)

    def test_isEvenlyDivisibleByAll232792560Limit10(self):
        self.assertEqual(problem5.isEvenlyDivisibleByAll(232792560, 10), True)

    def test_isEvenlyDivisibleByAll232792560Limit19(self):
        self.assertEqual(problem5.isEvenlyDivisibleByAll(232792560, 19), True)

    def test_isEvenlyDivisibleByAll232792560Limit20(self):
        self.assertEqual(problem5.isEvenlyDivisibleByAll(232792560, 20), True)

    def test_isEvenlyDivisibleByAll232792560Limit21(self):
        self.assertEqual(problem5.isEvenlyDivisibleByAll(232792560, 21), True)

    def test_isEvenlyDivisibleByAll232792560Limit22(self):
        self.assertEqual(problem5.isEvenlyDivisibleByAll(232792560, 22), True)

    def test_isEvenlyDivisibleByAll232792560Limit23(self):
        self.assertEqual(problem5.isEvenlyDivisibleByAll(232792560, 23), False)

    #sample provided in challenge
    def test_lowestEvenlyDivisibleByAll10(self):
        self.assertEqual(problem5.lowestEvenlyDivisibleByAll(10), 2520)

    #Solution needed to complete challenge
    def test_lowestEvenlyDivisibleByAll20(self):
        self.assertEqual(problem5.lowestEvenlyDivisibleByAll(20), 232792560)

    def test_lowestEvenlyDivisibleByAll22(self):
        self.assertEqual(problem5.lowestEvenlyDivisibleByAll(22), 232792560)

if __name__ == '__main__':
    unittest.main()