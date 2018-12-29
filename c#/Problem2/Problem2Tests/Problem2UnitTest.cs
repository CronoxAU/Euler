using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Problem2NS;

namespace Problem2Tests
{
    [TestClass]
    public class Problem2UnitTest
    {
        [TestMethod]
        public void sumEvenFibonacciFullResult()
        {
            //Test result for 4,000,000 ie the final solution
            // Arrange
            long expected = 4613732;
            long upperLimit = 4000000;
            // Act
            long actual = Problem2Class.sumEvenFibonacci(upperLimit);
            // Assert
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 4,000,000");
        }

        //****** sample cases *******
        [TestMethod]
        public void sumEvenFibonacciLimit7()
        {
            long expected = 2;
            long upperLimit = 7;
            long actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 7");
        }

        [TestMethod]
        public void sumEvenFibonacciLimit9()
        {
            long expected = 10;
            long upperLimit = 9;
            long actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 9");
        }

        [TestMethod]
        public void sumEvenFibonacciLimit34()
        {
            long expected = 10;
            long upperLimit = 34;
            long actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 34");
        }

        [TestMethod]
        public void sumEvenFibonacciLimit145()
        {
            long expected = 188;
            long upperLimit = 145;
            long actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 145");
        }

        //****** Edge cases *******
        [TestMethod]
        public void sumEvenFibonacciEdgeCaseLimitNegative()
        {

            long expected = 0;
            long upperLimit = -1;
            long actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of -1");
        }

        [TestMethod]
        public void sumEvenFibonacciEdgeCaseLimit0()
        {
            long expected = 0;
            long upperLimit = 0;
            long actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 0");
        }

        [TestMethod]
        public void sumEvenFibonacciEdgeCaseLimit1()
        {
            long expected = 0;
            long upperLimit = 1;
            long actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 1");
        }

        [TestMethod]
        public void sumEvenFibonacciEdgeCaseLimit2()
        {
            long expected = 0;
            long upperLimit = 2;
            long actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 2");
        }

        [TestMethod]
        public void sumEvenFibonacciEdgeCaseLimit3()
        {
            long expected = 2;
            long upperLimit = 3;
            long actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 3");
        }
    }
}
