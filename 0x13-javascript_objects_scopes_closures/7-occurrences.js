#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let out = 0;
  let i;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      out++;
    }
  }
  return (out);
}

module.exports.nbOccurences = nbOccurences;
