#!/usr/bin/node
// script that imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.
const dict = require('./101-data.js').dict;

const usersOccur = {};

for (const id in dict) {
  const occur = dict[id];

  if (occur in usersOccur) {
    usersOccur[occur].push(id);
  } else {
    usersOccur[occur] = [id];
  }
}

console.log(usersOccur);
