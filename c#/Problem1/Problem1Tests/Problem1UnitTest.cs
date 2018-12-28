using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Problem1NS;

namespace Problem1Tests
{
    [TestClass]
    public class Problem1UnitTest
    {
        [TestMethod]
        public void sumOfMultiplesHandlesBase1Upper1()
        {
            long expected = 0;
            long baseNumber = 1;
            long upperLimit = 1;
            long actual = Problem1Class.sumMultiples(baseNumber, upperLimit);
            Assert.AreEqual(expected, actual, "sumOfMultiples - Results not correct for base number " + baseNumber + ", upper limit " + upperLimit);
        }

        [TestMethod]
        public void sumOfMultiplesHandlesBase1Upper2()
        {
            long expected = 1;
            long baseNumber = 1;
            long upperLimit = 2;
            long actual = Problem1Class.sumMultiples(baseNumber, upperLimit);
            Assert.AreEqual(expected, actual, "sumOfMultiples - Results not correct for base number " + baseNumber + ", upper limit " + upperLimit);
        }

        [TestMethod]
        public void sumOfMultiplesHandlesBase0()
        {
            long expected = 0;
            long baseNumber = 0;
            long upperLimit = 100;
            long actual = Problem1Class.sumMultiples(baseNumber, upperLimit);
            Assert.AreEqual(expected, actual, "sumOfMultiples - Results not correct for base number " + baseNumber + ", upper limit " + upperLimit);
        }

        [TestMethod]
        public void sumOfMultiplesHandlesBaseNegative()
        {
            long expected = 0;
            long baseNumber = -50;
            long upperLimit = 100;
            long actual = Problem1Class.sumMultiples(baseNumber, upperLimit);
            Assert.AreEqual(expected, actual, "sumOfMultiples - Results not correct for base number " + baseNumber + ", upper limit " + upperLimit);
        }

        [TestMethod]
        public void sumOfMultiplesHandlesInitialSample()
        {
            long expected = 5;
            long baseNumber = 5;
            long upperLimit = 10;
            long actual = Problem1Class.sumMultiples(baseNumber, upperLimit);
            Assert.AreEqual(expected, actual, "sumOfMultiples - Results not correct for base number " + baseNumber + ", upper limit " + upperLimit);
        }

        [TestMethod]
        public void uniqueSumOfTwoMultiplesHandlesInitialSample()
        {
            long expected = 23;
            long number1 = 3;
            long number2 = 5;
            long upperLimit = 10;
            long actual = Problem1Class.uniqueSumOfTwoMultiples(number1, number2, upperLimit);
            Assert.AreEqual(expected, actual, "uniqueSumOfTwoMultiples - Results not correct for " + number1 + ", " + number2 + ", upper limit " + upperLimit);
        }

        [TestMethod]
        public void uniqueSumOfTwoMultiplesHandlesFinalAnswer()
        {
            long expected = 233168;
            long number1 = 3;
            long number2 = 5;
            long upperLimit = 1000;
            long actual = Problem1Class.uniqueSumOfTwoMultiples(number1, number2, upperLimit);
            Assert.AreEqual(expected, actual, "uniqueSumOfTwoMultiples - Results not correct for " + number1 + ", " + number2 + ", upper limit " + upperLimit);
        }
    }
}
