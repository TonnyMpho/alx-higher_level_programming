#!/usr/bin/node
// function that returns the reversed version of a list
// without using the built-in method reverse

exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
