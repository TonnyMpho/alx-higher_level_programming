#!/usr/bin/node
// script that prints a square

const n = parseInt(process.argv[2]);

if (!isNaN(n)) {
  for (let i = 0; i < n; i++) {
    console.log('x');
  }
} else {
  console.log('Missing size');
}
