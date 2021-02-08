#!/usr/bin/node
// Log me
let n = 0;
exports.logMe = function (item) {
  console.log(n + ': ' + item);
  n++;
};
