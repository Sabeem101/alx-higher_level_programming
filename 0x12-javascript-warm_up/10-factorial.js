#!/usr/bin/node
// Computes and prints a factorial.

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(process.argv[2]));
