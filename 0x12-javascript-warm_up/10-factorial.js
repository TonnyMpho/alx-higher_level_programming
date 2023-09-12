#!/usr/bin/node
// script that computes and prints a factorial

const num = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
