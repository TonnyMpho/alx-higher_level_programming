#!/usr/bin/node
// script that concats 2 files.
const fs = require('fs');

const firstFile = fs.readFileSync(process.argv[2]);
const secFile = fs.readFileSync(process.argv[3]);
const dstFile = process.argv[4];

fs.writeFileSync(dstFile, firstFile + secFile);
