#!/usr/bin/node
// script that imports an array and computes a new array.
const list = require('./100-data.js').list;

console.log(list);

const newList = list.map((n, i) => n * i);
console.log(newList);
