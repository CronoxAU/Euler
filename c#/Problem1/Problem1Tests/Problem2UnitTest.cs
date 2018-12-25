using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Problem1NS;

namespace Problem1Tests
{
    [TestClass]
    public class Problem2UnitTest
    {
        [TestMethod]
        public void sumOfMultiplesReturnsExpectedResult()
        {
            long expected = 0;
            long baseNumber = 1;
            long upperLimit = 1;
            long actual = Problem1Class.sumMultiples(baseNumber, upperLimit);
            Assert.AreEqual(expected, actual, "sumOfMultiples - Results not correct for base number " + baseNumber + ", upper limit " + upperLimit);

            expected = 1;
            baseNumber = 1;
            upperLimit = 2;
            actual = Problem1Class.sumMultiples(baseNumber, upperLimit);
            Assert.AreEqual(expected, actual, "sumOfMultiples - Results not correct for base number " + baseNumber + ", upper limit " + upperLimit);

            expected = 0;
            baseNumber = 0;
            upperLimit = 100;
            actual = Problem1Class.sumMultiples(baseNumber, upperLimit);
            Assert.AreEqual(expected, actual, "sumOfMultiples - Results not correct for base number " + baseNumber + ", upper limit " + upperLimit);

            expected = 0;
            baseNumber = -50;
            upperLimit = 100;
            actual = Problem1Class.sumMultiples(baseNumber, upperLimit);
            Assert.AreEqual(expected, actual, "sumOfMultiples - Results not correct for base number " + baseNumber + ", upper limit " + upperLimit);

            expected = 5;
            baseNumber = 5;
            upperLimit = 10;
            actual = Problem1Class.sumMultiples(baseNumber, upperLimit);
            Assert.AreEqual(expected, actual, "sumOfMultiples - Results not correct for base number " + baseNumber + ", upper limit " + upperLimit);
        }

        [TestMethod]
        public void uniqueSumOfTwoMultiplesReturnsExpectedResult()
        {
            long expected = 23;
            long number1 = 3;
            long number2 = 5;
            long upperLimit = 10;
            long actual = Problem1Class.uniqueSumOfTwoMultiples(number1, number2, upperLimit);
            Assert.AreEqual(expected, actual, "uniqueSumOfTwoMultiples - Results not correct for " + number1 + ", " + number2 + ", upper limit " + upperLimit);

            expected = 233168;
            number1 = 3;
            number2 = 5;
            upperLimit = 1000;
            actual = Problem1Class.uniqueSumOfTwoMultiples(number1, number2, upperLimit);
            Assert.AreEqual(expected, actual, "uniqueSumOfTwoMultiples - Results not correct for " + number1 + ", " + number2 + ", upper limit " + upperLimit);
        }
    }
}
