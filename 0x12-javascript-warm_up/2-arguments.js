#!/usr/bin/node
const args = process.argv;
const argc = args.length;

if (argc === 2) {
  console.log('No argument');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
