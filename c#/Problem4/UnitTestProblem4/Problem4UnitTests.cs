using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Problem4NS;


namespace UnitTestProblem4
{
    [TestClass]
    public class Problem4UnitTests
    {
        [TestMethod]
        public void makePlaindrome4Test()
        {
            int expected = 44;
            int input = 4;
            int actual = Problem4Class.makePlaindrome(input);
            Assert.AreEqual(expected, actual, "makePlaindrome - Results not correct for " + input);
        }

        [TestMethod]
        public void makePlaindrome23Test()
        {
            int expected = 2332;
            int input = 23;
            int actual = Problem4Class.makePlaindrome(input);
            Assert.AreEqual(expected, actual, "makePlaindrome - Results not correct for " + input);
        }

        [TestMethod]
        public void makePlaindrome752Test()
        {
            int expected = 752257;
            int input = 752;
            int actual = Problem4Class.makePlaindrome(input);
            Assert.AreEqual(expected, actual, "makePlaindrome - Results not correct for " + input);
        }

        [TestMethod]
        public void isProductOfTwo3DigitNumbers100Test()
        {
            Boolean expected = false;
            int input = 100;
            Boolean actual = Problem4Class.isProductOfTwo3DigitNumbers(input);
            Assert.AreEqual(expected, actual, "isProductOfTwo3DigitNumbers - Results not correct for " + input);
        }

        [TestMethod]
        public void isProductOfTwo3DigitNumbers9999Test()
        {
            Boolean expected = false;
            int input = 9999;
            Boolean actual = Problem4Class.isProductOfTwo3DigitNumbers(input);
            Assert.AreEqual(expected, actual, "isProductOfTwo3DigitNumbers - Results not correct for " + input);
        }

        [TestMethod]
        public void isProductOfTwo3DigitNumbers10000Test()
        {
            Boolean expected = true;
            int input = 100*100;
            Boolean actual = Problem4Class.isProductOfTwo3DigitNumbers(input);
            Assert.AreEqual(expected, actual, "isProductOfTwo3DigitNumbers - Results not correct for " + input);
        }

        [TestMethod]
        public void isProductOfTwo3DigitNumbers10001Test()
        {
            Boolean expected = false;
            int input = 10001;
            Boolean actual = Problem4Class.isProductOfTwo3DigitNumbers(input);
            Assert.AreEqual(expected, actual, "isProductOfTwo3DigitNumbers - Results not correct for " + input);
        }

        [TestMethod]
        public void getFirstHalf658945Test()
        {
            int expected = 658;
            int input = 658945;
            int actual = Problem4Class.getFirstHalf(input);
            Assert.AreEqual(expected, actual, "getFirstHalf - Results not correct for " + input);
        }

        [TestMethod]
        public void findLargestPalindromeProductOfTwo3DigitNumbersFullProblemTest()
        {
            int expected = 906609;
            int input = 999*999;
            int actual = Problem4Class.findLargestPalindromeProductOfTwo3DigitNumbers(input);
            Assert.AreEqual(expected, actual, "isProductOfTwo3DigitNumbers - Results not correct for " + input);
        }

    }
}
