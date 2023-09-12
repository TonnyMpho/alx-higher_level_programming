#!/usr/bin/node
// script that prints a square

const n = parseInt(process.argv[2]);
let squares = '';

if (!isNaN(n)) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      squares += 'X';
    }
    if (i < (n - 1)) {
      squares += '\n';
    }
  }
  console.log(squares);
} else {
  console.log('Missing size');
}
