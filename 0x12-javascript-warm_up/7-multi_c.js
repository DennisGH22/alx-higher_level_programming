#!/usr/bin/node
const args = process.argv.slice(2);
const firstArgument = parseInt(args[0], 10);

if (!isNaN(firstArgument)) {
  for (let i = 0; i < firstArgument; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
