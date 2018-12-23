//Solution to Project Euler problem 1
//Find the sum of all the multiples of 3 or 5 below 1000.
let sumThreeAndFive;
sumThreeAndFive = sumOf3And5Multiples(1000);
console.log(sumThreeAndFive);

function sumOf3And5Multiples(sumTo){
  let sum = 0;
  let i = 1;
  //sum all the multiples of 3
  for (i = 3; i < sumTo; i += 3){
    sum += i;
  }
  //sum all of the multiples of 5, as long as they are not also multiples of 3
  for (i = 5; i < sumTo; i += 5){
    if(i % 3 !== 0){
      sum += i;
    }
  }
  return sum;
}