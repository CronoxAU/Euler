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


if __name__ == '__main__':
    unittest.main()