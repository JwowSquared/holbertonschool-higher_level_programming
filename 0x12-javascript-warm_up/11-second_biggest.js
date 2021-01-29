#!/usr/bin/node
const args = process.argv;
const argc = args.length;
let out, max, i;

if (argc < 4) {
  console.log(0);
} else {
  max = args[2];
  for (i = 3; i < argc; i++) {
    if (max <= args[i]) {
      out = max;
      max = args[i];
    }
  }
  console.log(out);
}
