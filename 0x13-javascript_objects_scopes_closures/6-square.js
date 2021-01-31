#!/usr/bin/node

const Base = require('./5-square');

class Square extends Base {

  charPrint (c) {
    let i;
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
