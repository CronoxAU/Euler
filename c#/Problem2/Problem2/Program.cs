using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Solution to Project Euler problem 2
//Find the sum of all even Fibonacci numbers below 4,000,000

namespace Problem2
{
    class Program
    {
        static void Main(string[] args)
        {
            long result = sumEvenFibonacci(4000000);
            //output the result and keep the console open until the user presses a buton
            Console.WriteLine(result);
            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }

        static long sumEvenFibonacci(long upperLimit)
        {
            long current = 1; //the current number in the sequence
            long previous1 = 0; //the previous number in the sequence
            long previous2 = 1; //the previous number in the sequence
            long sum = 0; //the running total

            //continue checking each fib number until we reach the upper limit.
            while (current < upperLimit)
            {
                current = previous1 + previous2; //get the new current value
                //update the previous value
                previous2 = previous1;
                previous1 = current;
                Console.WriteLine(current);
                //check if the current number is even and only include it if it is
                if (current % 2 == 0)
                {
                    sum += current;
                }
            }
            return sum;
        }
    }
}
