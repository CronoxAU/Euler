using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Solution to Project Euler problem 4 - https://projecteuler.net/problem=4
//Find the largest palindrome made from the product of two 3-digit numbers.

namespace Problem4NS
{
    public class Problem4Class
    {
        static void Main(string[] args)
        { 
            int result = findLargestPalindromeProductOfTwo3DigitNumbers(999 * 999);
            Console.WriteLine(result);

            // Keep the console window open in debug mode.
            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }

        //reverses the supplied string
        public static string reverseString(string s)
        {
            char[] arr = s.ToCharArray();
            Array.Reverse(arr);
            return new string(arr);
        }

        //return a palindrome here the prefix is the first digits
        public static int makePlaindrome(int prefix)
        {
            string strPrefix = prefix.ToString();
            string strSuffix = reverseString(strPrefix);
            return Int32.Parse(strPrefix + strSuffix);
        }

        //returns true if the supplied num is the product of 2 three digit numbers
        public static Boolean isProductOfTwo3DigitNumbers(int num)
        {
            int upperLimit = (int)(Math.Sqrt(num));
            Boolean result = false;
            if(upperLimit < 1000 && upperLimit >= 100)
            {
                for(int i = upperLimit; i >= 100; i--)
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

        public static int getFirstHalf(int num)
        {
            string numString = num.ToString();
            string firstHalf = (numString.Substring(0, numString.Length/2));
            return Int32.Parse(firstHalf);
        }

        //This function only works on on 6 digit numbers.
        public static int findLargestPalindromeProductOfTwo3DigitNumbers(int upperLimit)
        {
            Boolean found = false;
            int i = 0;
                int firstHalf = getFirstHalf(upperLimit);
                while (!found && firstHalf > 100)
                {
                    i = makePlaindrome(firstHalf);
                    if (isProductOfTwo3DigitNumbers(i))
                    {
                        found = true;
                    }
                    firstHalf--;
                }
            return i;
            
        }
    }
}
