#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let n = 0;

  for (const i in list) {
    if (list[i] === searchElement) {
      n++;
    }
  }
  return (n);
};
