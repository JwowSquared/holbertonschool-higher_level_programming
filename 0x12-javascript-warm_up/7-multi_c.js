#!/usr/bin/node
const args = process.argv;
let i = 0;

if (!isNaN(args[2])) {
  for (i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
