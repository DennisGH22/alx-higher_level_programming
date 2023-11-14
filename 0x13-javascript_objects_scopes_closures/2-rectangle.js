#!/usr/bin/node
class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
