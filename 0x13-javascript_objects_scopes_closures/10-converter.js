#!/usr/bin/node

function converter (base) {
  function engine (num) {
    return (num.toString(base));
  }
  return (engine);
}

module.exports.converter = converter;
