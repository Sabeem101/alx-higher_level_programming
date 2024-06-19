#!/usr/bin/node
/*
 * Square class prints the rectangle using the character c.
 */
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let a = 0; a < this.height; a++) console.log(c.repeat(this.width));
    }
  }
};
