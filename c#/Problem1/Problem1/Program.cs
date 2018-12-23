using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


//Solution to Project Euler problem 1
//Find the sum of all the multiples of 3 or 5 below 1000.

namespace Problem1
{
    class Program
    {
        static void Main(string[] args)
        {
            long sumThreeAndFive = sumOf3And5Multiples(1000);
            Console.WriteLine(sumThreeAndFive);

            // Keep the console window open in debug mode.
            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }

        static long sumOf3And5Multiples(long sumTo)
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
