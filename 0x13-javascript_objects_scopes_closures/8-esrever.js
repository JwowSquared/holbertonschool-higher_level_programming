#!/usr/bin/node

function esrever (list) {
  let i;
  let temp;

  for (i = 0; i < list.length / 2; i++) {
    temp = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = temp;
  }
  return (list);
}

module.exports.esrever = esrever;
