#!/usr/bin/node

let left = 0;

function logMe (item) {
  console.log(String(left++) + ': ' + item);
}

module.exports.logMe = logMe;
