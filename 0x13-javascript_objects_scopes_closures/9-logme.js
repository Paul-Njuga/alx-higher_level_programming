#!/usr/bin/node
let count = 0;

exports.logMe = function (item) {
  if (item) {
    ++count;
    console.log(count + ': ' + item);
  }
};
