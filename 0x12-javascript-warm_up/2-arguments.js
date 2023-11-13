#!/usr/bin/node
const { argv } = require('node:process');

let message;

argv.forEach((element) => {
  if (!argv[2]) {
    message = 'No Argument';
  } else if (argv[2] && !argv[3]) {
    message = 'Argument Found';
  } else {
    message = 'Arguments Found';
  }
});

console.log(message);
