import unittest
import problem4

class Test_TestProblem4(unittest.TestCase):

    def test_isPalindrome10(self):
        self.assertEqual(problem4.isPalindrome(10), False)

    def test_isPalindrome11(self):
        self.assertEqual(problem4.isPalindrome(11), True)

    def test_isPalindrome9009(self):
        self.assertEqual(problem4.isPalindrome(9009), True)

    def test_isPalindrome9010(self):
        self.assertEqual(problem4.isPalindrome(9010), False)

    def test_makePalindrome90(self):
        self.assertEqual(problem4.makePalindrome(90), 9009)

    def test_makePalindrome989(self):
        self.assertEqual(problem4.makePalindrome(989), 989989)

    def test_makePalindrome987(self):
        self.assertEqual(problem4.makePalindrome(987), 987789)

    def test_getFirstHalf987654(self):
        self.assertEqual(problem4.getFirstHalf(987654), 987)

    def test_getFirstHalf3215(self):
        self.assertEqual(problem4.getFirstHalf(3215), 32)

    def test_isProductOfTwo3DigitNumbers10(self):
        self.assertEqual(problem4.isProductOfTwo3DigitNumbers(10), False)

    def test_isProductOfTwo3DigitNumbers100000(self):
        self.assertEqual(problem4.isProductOfTwo3DigitNumbers(100000), True)

    def test_isProductOfTwo3DigitNumbers100001(self):
        self.assertEqual(problem4.isProductOfTwo3DigitNumbers(100001), False)

    def test_isProductOfTwo3DigitNumbers899Squared(self):
        self.assertEqual(problem4.isProductOfTwo3DigitNumbers(899*899), True)

    def test_FinalSolution(self):
        self.assertEqual(problem4.findLargestPalindromeProductOfTwo3DigitNumbers(999*999), 906609)

if __name__ == '__main__':
    unittest.main()