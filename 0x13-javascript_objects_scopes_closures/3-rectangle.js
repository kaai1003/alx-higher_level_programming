#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const symb = 'X';
    let i = 0;
    while (i < this.height) {
      console.log(symb.repeat(this.width));
      i++;
    }
  }
};
