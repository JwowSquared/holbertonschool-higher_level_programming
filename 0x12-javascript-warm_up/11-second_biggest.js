#!/usr/bin/node
const args = process.argv;
const argc = args.length;
let out, max, i;

if (argc < 4) {
  console.log(0);
} else {
  max = args[2];
  if (max >= args[3]) {
    out = args[3];
  }
  for (i = 4; i < argc; i++) {
    if (max <= args[i]) {
      out = max;
      max = args[i];
    }
  }
  console.log(out);
}
