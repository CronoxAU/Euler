//Solution to Project Euler problem 2
//Find the sum of all even Fibonacci numbers below 4,000,000

const result = sumEvenFibonacci(4000000);
console.log(result);

function sumEvenFibonacci(upperLimit) {
  let current = 1; //the current number in the sequence
  let previous1 = 0; //the previous number in the sequence
  let previous2 = 1; //the previous number in the sequence
  let sum = 0; //the running total

  //continue checking each fib number until we reach the upper limit.
  while (current < upperLimit) {
    current = previous1 + previous2; //get the new current value
    //update the previous value
    previous2 = previous1;
    previous1 = current;
    //console.log(current);
    //check if the current number is even and only include it if it is
    if (current % 2 == 0) {
      sum += current;
    }
  }
  return sum;
}