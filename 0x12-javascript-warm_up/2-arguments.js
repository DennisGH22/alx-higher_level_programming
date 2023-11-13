#!/usr/bin/node
const { argv } = require('node:process');

let message;

argv.forEach(() => {
  if (!argv[2]) {
    message = 'No argument';
  } else if (argv[2] && !argv[3]) {
    message = 'Argument found';
  } else {
    message = 'Arguments found';
  }
});

console.log(message);
