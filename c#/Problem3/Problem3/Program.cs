﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Solution to Project Euler problem 3 - https://projecteuler.net/problem=3
//What is the largest prime factor of the number 600851475143.

namespace Problem3NS
{
    public class Problem3Class
    {
        static void Main(string[] args)
        {
            long result = largestPrimeFactor(600851475143);
            Console.WriteLine(result);

            // Keep the console window open in debug mode.
            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }

        //returns the largest prime factor of the supplied number
        //returns 0 if the number has no prime factor
        public static long largestPrimeFactor(long num)
        {
            long primeFactor = 0;
            //find the upper limit of values ot test
            long upperLimit = num/2;
            for(long i = upperLimit; i > 0; i--)
            {
                if(num % i == 0)
                {
                    if (isPrime(i))
                    {
                        return i;
                    }
                }
            }
            return primeFactor;
        }

        //return true if the supplied number is prime
        public static Boolean isPrime(long num)
        {
            if (num <= 1) return false;
            if (num % 2 == 0) return false;
            //find the upper limit of values ot test
            long upperLimit = (long)Math.Sqrt(num);
            //loop through each potential odd factor, and return false if a factor is found
            for(long i = 3; i <= upperLimit; i+=2)
            {
                if (num % i == 0) return false;
            }
            //if no factor is found, return true
            return true;
        }
    }
}
