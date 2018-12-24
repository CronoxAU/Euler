using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Problem2NS;

namespace Problem2Tests
{
    [TestClass]
    public class Problem2UnitTest
    {
        [TestMethod]
        public void sumEvenFibonacciReturnsExpectedResult()
        {
            //Test result for 4,000,000 ie the final solution
            // Arrange
            long expected = 4613732;
            long upperLimit = 4000000;
            // Act
            long actual = Problem2Class.sumEvenFibonacci(upperLimit);
            // Assert
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 4,000,000");


            //****** Sample cases *******
            expected = 2;
            upperLimit = 7;
            actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 7");

            expected = 10;
            upperLimit = 9;
            actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 9");

            expected = 10;
            upperLimit = 34;
            actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 34");

            expected = 44;
            upperLimit = 35;
            actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 35");

            expected = 188;
            upperLimit = 145;
            actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 145");


            //****** Edge cases *******
            //Test result for a negetive number
            expected = 0;
            upperLimit = -1;
            actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of -1");

            //Test result for 0
            expected = 0;
            upperLimit = 0;
            actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 0");

            //Test result for 1
            expected = 0;
            upperLimit = 1;
            actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 1");
            
            //Test result for 2
            expected = 0;
            upperLimit = 2;
            actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 2");

            //Test result for 3
            expected = 2;
            upperLimit = 3;
            actual = Problem2Class.sumEvenFibonacci(upperLimit);
            Assert.AreEqual(expected, actual, "Results not correct for upper limit of 3");
        }
    }
}
