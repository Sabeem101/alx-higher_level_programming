#!/usr/bin/node
/*
 * Printing the rectangle class.
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let b = 0;
      let myVar = '';
      while (b < this.width) {
        myVar += 'X';
        b++;
      }
      console.log(myVar);
    }
  }
}
module.exports = Rectangle;
