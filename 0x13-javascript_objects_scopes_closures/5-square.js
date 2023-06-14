#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

/* Creates class Square that extends class Rectangle */
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
