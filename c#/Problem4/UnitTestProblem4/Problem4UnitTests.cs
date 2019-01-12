using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Problem4NS;


namespace UnitTestProblem4
{
    [TestClass]
    public class Problem4UnitTests
    {
        [TestMethod]
        public void isPalindrome10Test()
        {
            Boolean expected = false;
            long number = 4;
            Boolean actual = Problem4Class.isPalindrome(number);
            Assert.AreEqual(expected, actual, "isPalindrome - Results not correct for " + number);
        }
    }
}
