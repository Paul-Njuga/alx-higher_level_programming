#!/usr/bin/node
const cSquare = require('./5-square.js');

/* Creates class Square that extends class Square */
module.exports = class Square extends cSquare {
  charPrint (C) {
    if (C == null) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
