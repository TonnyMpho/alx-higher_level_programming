#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const integers = [];
for (let i = 2; i < process.argv.length; i++) {
  integers.push(parseInt(process.argv[i]));
}

if (integers.length < 3) {
  console.log(0);
} else {
  integers.sort((a, b) => b - a);
  console.log(integers[1]);
}
