#!/usr/bin/node
let message;

argv.forEach(() => {
  if (process.argv.slice(2).length === 0) {
    message = 'No argument';
  } else if (process.argv.slice(2).length === 1) {
    message = 'Argument found';
  } else {
    message = 'Arguments found';
  }
});

console.log(message);
