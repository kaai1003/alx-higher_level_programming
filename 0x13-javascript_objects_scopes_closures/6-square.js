#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let symb;
    if (c) {
      symb = c;
    } else {
      symb = 'X';
    }
    let i = 0;
    while (i < this.height) {
      console.log(symb.repeat(this.width));
      i++;
    }
  }
};
