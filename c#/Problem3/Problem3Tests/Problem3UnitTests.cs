using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Problem3NS;

namespace Problem3Tests
{
    [TestClass]
    public class Problem3UnitTests
    {
        [TestMethod]
        public void isPrime1Test()
        {
            Boolean expected = false;
            long number = 1;
            Boolean actual = Problem3Class.isPrime(number);
            Assert.AreEqual(expected, actual, "isPrime - Results not correct for " + number);
        }

        [TestMethod]
        public void isPrime2Test()
        {
            Boolean expected = false;
            long number = 2;
            Boolean actual = Problem3Class.isPrime(number);
            Assert.AreEqual(expected, actual, "isPrime - Results not correct for " + number);
        }

        [TestMethod]
        public void isPrime5Test()
        {
            Boolean expected = true;
            long number = 5;
            Boolean actual = Problem3Class.isPrime(number);
            Assert.AreEqual(expected, actual, "isPrime - Results not correct for " + number);
        }

        [TestMethod]
        public void isPrime13Test()
        {
            Boolean expected = true;
            long number = 13;
            Boolean actual = Problem3Class.isPrime(number);
            Assert.AreEqual(expected, actual, "isPrime - Results not correct for " + number);
        }

        [TestMethod]
        public void isPrime109Test()
        {
            Boolean expected = true;
            long number = 109;
            Boolean actual = Problem3Class.isPrime(number);
            Assert.AreEqual(expected, actual, "isPrime - Results not correct for " + number);
        }

        [TestMethod]
        public void isPrime199Test()
        {
            Boolean expected = true;
            long number = 199;
            Boolean actual = Problem3Class.isPrime(number);
            Assert.AreEqual(expected, actual, "isPrime - Results not correct for " + number);
        }

        [TestMethod]
        public void largestPrimeFactor13195Test()
        {
            long expected = 29;
            long number = 13195;
            long actual = Problem3Class.largestPrimeFactor(number);
            Assert.AreEqual(expected, actual, "largestPrimeFactor - Results not correct for " + number);
        }

        [TestMethod]
        public void largestPrimeFactor600851475143Test()
        {
            long expected = 6857;
            long number = 600851475143;
            long actual = Problem3Class.largestPrimeFactor(number);
            Assert.AreEqual(expected, actual, "largestPrimeFactor - Results not correct for " + number);
        }
    }
}
