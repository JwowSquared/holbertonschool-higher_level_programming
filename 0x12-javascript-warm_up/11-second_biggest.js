#!/usr/bin/node
const args = process.argv;
const argc = args.length;
const nums = [];
let i;

if (argc < 4) {
  console.log(0);
} else {
  for (i = 2; i < argc; i++) {
    nums.push(Number(args[i]));
  }
  nums.sort();
  console.log(nums[argc - 4]);
}
