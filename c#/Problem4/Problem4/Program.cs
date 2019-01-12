using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Solution to Project Euler problem 4 - https://projecteuler.net/problem=4
//Find the largest palindrome made from the product of two 3-digit numbers.

namespace Problem4NS
{
    class Problem4Class
    {
        static void Main(string[] args)
        {
        }

        //reverses the supplied string
        public static string reverseString(string s)
        {
            char[] arr = s.ToCharArray();
            Array.Reverse(arr);
            return new string(arr);
        }

        //return true if the supplied string is a palindrome
        public static string makePlaindrome(string prefix)
        {
            string suffix = reverseString(prefix);
            return prefix + suffix;
        }

        //returns true if the supplied num is the product of 2 three digit numbers
        public static Boolean isProductOfTwo3DigitNumbers(int num)
        {
            int upperLimit = (int)(Math.Sqrt(num));
            Boolean result = false;
            if(upperLimit > 1000 && upperLimit < 100)
            {
                for(int i = upperLimit; i < 100; i--)
                {
                    if(num % i == 0)
                    {
                        int j = num / i;
                        if (j >= 100 && j < 1000 && num % j == 0)
                        {
                            result = true;
                            break;
                        }
                    }
                }
            }
            return result;
        }

        public static int getFirstHalf(num)
        {

        }

        public static int findLargestPalindromeProductOfTwo3DigitNumbers(int upperLimit)
        {
            Boolean found = false;
            int initialFirstHalf = Int32.Parse(upperLimit.ToString().Substring(0, 5));
        }
    }
}
