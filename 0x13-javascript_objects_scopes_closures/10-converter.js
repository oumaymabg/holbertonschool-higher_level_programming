#!/usr/bin/node
// Write a function that converts a number from base 10 to another base passed as argument
exports.converter = function (base) {
  return function mainConvert (num) {
    return num.toString(base);
  };
};
