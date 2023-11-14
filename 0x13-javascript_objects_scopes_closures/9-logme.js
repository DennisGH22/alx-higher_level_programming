#!/usr/bin/node
let numberOfArguments = 0;

module.exports.logMe = function (item) {
  console.log(`${numberOfArguments}: ${item}`);
  numberOfArguments++;
};
