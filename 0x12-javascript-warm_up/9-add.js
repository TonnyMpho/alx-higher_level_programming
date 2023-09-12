#!/usr/bin/node
// script that prints the addition of 2 integers

const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(n1, n2);
