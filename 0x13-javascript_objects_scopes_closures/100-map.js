#!/usr/bin/node
const initialList = require('./100-data').list;

const newList = initialList.map((value, index) => value * index);

console.log(initialList);
console.log(newList);
