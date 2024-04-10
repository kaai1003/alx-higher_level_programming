#!/usr/bin/node
const newSquare = require('./5-square');
module.exports = class Square extends newSquare {
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
