#!/usr/bin/node
const dict = require('./101-data').dict;

const out = {};

for (const [key, value] of Object.entries(dict)) {
  if (value in out) {
    out[value].push(key);
  } else {
    out[value] = [key];
  }
}

console.log(out);
