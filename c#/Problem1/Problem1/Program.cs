using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


//Solution to Project Euler problem 1
//Find the sum of all the multiples of 3 or 5 below 1000.

namespace Problem1NS
{
    public class Problem1Class
    {
        public static void Main(string[] args)
        {
            
            long result = uniqueSumOfTwoMultiples(3, 5, 1000);
            Console.WriteLine(result);

            // Keep the console window open in debug mode.
            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }

        public static long uniqueSumOfTwoMultiples(long number1, long number2, long upperLimit)
        {
            //add the sum of the multipules of the two supplied numbers, and subtract the sum of their factor
            return sumMultiples(number1, upperLimit) + sumMultiples(number2, upperLimit) - sumMultiples(number2 * number1, upperLimit);
        }

        //returns the sum of all multipules of baseNumber up to upperLimit
        //only accepts positive values for baseNumber and upperLimit, returns 0 otherwise.
        public static long sumMultiples(long baseNumber, long upperLimit)
        {
            long sum = 0;
            long i;

            if(baseNumber > 0 && upperLimit > 0 && baseNumber < upperLimit)
            { 
                for (i = baseNumber; i < upperLimit; i += baseNumber)
                {
                    sum += i;
                }
            }
            return sum;
        }


        //old function that is no longer used as it was too specific.
        public static long sumOf3And5Multiples(long sumTo)
        {
            long sum = 0;
            long i;
            //sum all the multiples of 3
            for (i = 3; i < sumTo; i += 3)
            {
                sum += i;
            }
            //sum all of the multiples of 5, as long as they are not also multiples of 3
            for (i = 5; i < sumTo; i += 5)
            {
                if (i % 3 != 0)
                {
                    sum += i;
                }
            }
            return sum;
        }
    }
}
