#!/usr/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');
const file = process.argv[2];

const data = fs.readFileSync(file, "utf-8");
console.log(data);
