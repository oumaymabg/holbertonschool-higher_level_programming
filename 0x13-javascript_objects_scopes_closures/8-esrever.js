#!/usr/bin/node
// Write a function that returns the reversed version of a list
exports.esrever = function (list) {
  const res = [];
  for (let i = list.length - 1; i >= 0; i--) {
    res.push(list[i]);
  }
  return res;
};
