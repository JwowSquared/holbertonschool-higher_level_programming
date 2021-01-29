#!/usr/bin/node
const args = process.argv;
let left = 'undefined';
let right = 'undefined';

if (args[2]) {
  left = args[2];
}
if (args[3]) {
  right = args[3];
}

console.log(left + ' is ' + right);
