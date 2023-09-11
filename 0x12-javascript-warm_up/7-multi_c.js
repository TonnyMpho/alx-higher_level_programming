#!/usr/bin/node
// script that prints x times “C is fun"

const arg = process.argv[2];

if (!isNaN(arg)) {
  for (let i = 0; i < parseInt(arg); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
